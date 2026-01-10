import tensorflow as tf
from tensorflow.keras import layers, models
import os

# ============================================================
# CONFIG
# ============================================================
DATASET_ROOT = "./dataset"
TRAIN_DIR = os.path.join(DATASET_ROOT, "train")
VAL_DIR   = os.path.join(DATASET_ROOT, "val")

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# ============================================================
# CLASS MAP
# ============================================================
CLASS_NAMES = sorted(os.listdir(TRAIN_DIR))
CLASS_TO_ID = {name: idx for idx, name in enumerate(CLASS_NAMES)}
NUM_CLASSES = len(CLASS_NAMES)

print("Class map:", CLASS_TO_ID)

# ============================================================
# DATASET BUILDER
# ============================================================
def build_dataset(root_dir):

    image_paths = []
    labels = []

    for cls_name, cls_id in CLASS_TO_ID.items():
        cls_dir = os.path.join(root_dir, cls_name)

        for f in os.listdir(cls_dir):
            if f.lower().endswith(".jpg"):
                image_paths.append(os.path.join(cls_dir, f))
                labels.append(cls_id)

    image_paths = tf.constant(image_paths, dtype=tf.string)
    labels = tf.constant(labels, dtype=tf.int32)

    ds = tf.data.Dataset.from_tensor_slices((image_paths, labels))

    def parse_image(path, label):
        img = tf.io.read_file(path)
        img = tf.image.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, IMG_SIZE)
        img = tf.cast(img, tf.float32) / 255.0
        return img, label

    ds = ds.map(parse_image, num_parallel_calls=tf.data.AUTOTUNE)
    ds = ds.shuffle(1000).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

    return ds

train_ds = build_dataset(TRAIN_DIR)
val_ds   = build_dataset(VAL_DIR)

print("Train samples:", sum(1 for _ in train_ds))
print("Val samples  :", sum(1 for _ in val_ds))

# ============================================================
# MobileNetV3 Small
# ============================================================
def SEBlock(x, reduction=4):
    filters = x.shape[-1]
    se = layers.GlobalAveragePooling2D()(x)
    se = layers.Reshape((1,1,filters))(se)
    se = layers.Conv2D(filters//reduction, 1, activation='relu')(se)
    se = layers.Conv2D(filters, 1, activation='sigmoid')(se)
    return layers.Multiply()([x, se])

def MBConv(x, out_channels, kernel, stride, expand_ratio, use_se):
    in_ch = x.shape[-1]
    hidden = in_ch * expand_ratio

    if expand_ratio != 1:
        x = layers.Conv2D(hidden,1,padding='same',use_bias=False)(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation('swish')(x)

    x = layers.DepthwiseConv2D(kernel,strides=stride,padding='same',use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('swish')(x)

    if use_se:
        x = SEBlock(x)

    x = layers.Conv2D(out_channels,1,padding='same',use_bias=False)(x)
    x = layers.BatchNormalization()(x)

    if stride == 1 and in_ch == out_channels:
        return layers.Add()([x, x])
    return x

def MobileNetV3_Small():
    inputs = layers.Input(shape=(224,224,3))
    x = layers.Conv2D(16,3,strides=2,padding='same',use_bias=False)(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)

    x = MBConv(x,16,3,2,1,True)
    x = MBConv(x,24,3,2,4,False)
    x = MBConv(x,40,5,2,3,True)
    x = MBConv(x,96,5,2,6,True)

    x = layers.Conv2D(576,1,use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(1024,activation='relu')(x)
    outputs = layers.Dense(NUM_CLASSES,activation='softmax')(x)

    return models.Model(inputs,outputs)

# ============================================================
# TRAIN
# ============================================================
model = MobileNetV3_Small()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_ds, validation_data=val_ds, epochs=10)
model.save("mobilenet.keras")
