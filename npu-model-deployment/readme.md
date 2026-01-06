## Running Models with TensorFlow Lite Python API

All `.tflite` models follow the same execution flow.

---

### 1. Load the Model
```text
from tensorflow.lite.python.interpreter import Interpreter

interpreter = Interpreter(model_path="model.lne")
interpreter.allocate_tensors()
```
### 2. Get Input and Output Details
```text
input_details  = interpreter.get_input_details()
output_details = interpreter.get_output_details()
These provide the tensor index, shape, and datatype required for inference.
```
### 3. Set the Input to the Model
```text
import cv2
import numpy as np

image = cv2.imread("test.jpg")
image = cv2.resize(image, (224, 224))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = np.expand_dims(image, axis=0).astype(np.float32) / 255.0

interpreter.set_tensor(input_details[0]['index'], image)
```
### 4. Invoke the Model
```text
interpreter.invoke()
This executes the inference.
```
### 5. Get the Output Results
```text
output = interpreter.get_tensor(output_details[0]['index'])
print(output)
```