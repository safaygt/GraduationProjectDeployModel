from flask import Flask, request, jsonify, send_from_directory
from ultralytics import YOLO
import os
import torch
from PIL import Image
import uuid

app = Flask(__name__)

from flask_cors import CORS
CORS(app)

MODEL_PATH = "/app/my_model.pt"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model dosyası bulunamadı: {MODEL_PATH}")

model = YOLO(MODEL_PATH)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed_images"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(PROCESSED_FOLDER):
    os.makedirs(PROCESSED_FOLDER)

CLASS_NAMES = ['glass', 'metal', 'paper', 'plastic']

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Dosya bulunamadı"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Dosya seçilmedi"}), 400

    unique_filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(filepath)

    results = model(filepath)

    detections = []
    class_counts = {}
    for result in results:
    
        processed_image_filename = f"processed_{unique_filename}"
        processed_image_path = os.path.join(PROCESSED_FOLDER, processed_image_filename)

     
        result.save(filename=processed_image_path)

        for box in result.boxes:
            class_id = int(box.cls.item())
            confidence = float(box.conf.item())
            x_min, y_min, x_max, y_max = map(float, box.xyxy[0].tolist())
            class_name = CLASS_NAMES[class_id]
            detections.append({
                "class_name": class_name,
                "confidence": confidence,
                "bbox": [x_min, y_min, x_max, y_max]
            })
            class_counts[class_name] = class_counts.get(class_name, 0) + 1

    processed_image_url = f"http://127.0.0.1:5000/processed_images/{processed_image_filename}"

    return jsonify({
        "detections": detections,
        "class_counts": class_counts,
        "processed_image_url": processed_image_url 
    })

@app.route("/processed_images/<filename>")
def get_processed_image(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False) 