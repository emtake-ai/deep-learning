from tensorflow.lite.python.interpreter import Interpreter
import cv2
import numpy as np

interpreter = Interpreter("model.tflite")
interpreter.allocate_tensors()

input_details  = interpreter.get_input_details()
output_details = interpreter.get_output_details()

img = cv2.imread("test.jpg")
img = cv2.resize(img, (224,224))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.expand_dims(img, axis=0).astype(np.float32) / 255.0

interpreter.set_tensor(input_details[0]['index'], img)
interpreter.invoke()

output = interpreter.get_tensor(output_details[0]['index'])
print(output)
