import numpy as np
import cv2
import time
import threading
from flask import Flask, Response, render_template_string
from lne_tflite import interpreter as lt

MODEL_PATH = "./LNE/Detection/mobilenet.lne"
CLASS_NAMES = ["dog", "cat", "person"]
IMG_SIZE = 224

# ================= LNE INIT (MUST BE FIRST) =================
print("[INIT] Loading LNE model...")
interpreter = lt.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details  = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Give ISP pipeline time to be ready
time.sleep(0.5)

# ================= CAMERA OPEN =================
print("[INIT] Opening camera...")
cap = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"BGR3"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

if not cap.isOpened():
    raise RuntimeError("Camera open failed")

frame_lock = threading.Lock()
output_frame = None

# ================= INFERENCE THREAD =================
def inference_loop():
    global output_frame
    print("[THREAD] Inference thread started")

    while True:
        ret, raw = cap.read()
        if not ret:
            print("[WARN] camera read failed → retry")
            cap.release()
            time.sleep(0.2)
            cap.open("/dev/video0")
            continue

        raw = raw.reshape((3, 360, 640))     # CHW
        frame = np.transpose(raw, (1, 2, 0)) # HWC
        frame = frame.copy()

        img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)

        interpreter.set_tensor(input_details[0]['index'], img)
        interpreter.invoke()

        out = interpreter.get_tensor(output_details[0]['index'])
        probs = np.squeeze(out).reshape(-1)

        class_id = int(np.argmax(probs))
        conf = float(probs[class_id])
        label = CLASS_NAMES[class_id]

        cv2.putText(frame, f"{label}: {conf*10:.1f}%", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        with frame_lock:
            output_frame = frame.copy()

# ================= FLASK =================
app = Flask(__name__)

HTML = """
<html>
<body>
<h2>LNE Camera AI Stream</h2>
<img src="/video">
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

def generate():
    global output_frame
    while True:
        with frame_lock:
            if output_frame is None:
                continue
            ret, buffer = cv2.imencode(".jpg", output_frame)
        if not ret:
            continue

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" +
               buffer.tobytes() + b"\r\n")

@app.route("/video")
def video():
    return Response(generate(),
        mimetype="multipart/x-mixed-replace; boundary=frame")

# ================= MAIN =================
if __name__ == "__main__":
    threading.Thread(target=inference_loop, daemon=True).start()
    print("[MAIN] Flask server started : http://<IP>:5000")
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=False)
