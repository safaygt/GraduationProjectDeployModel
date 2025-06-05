from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import torch
from PIL import Image
import uuid

app = Flask(__name__)

# CORS'u aç
from flask_cors import CORS
CORS(app)

# Modeli yükle
MODEL_PATH = "C:\\Users\\safay\\OneDrive\\Masaüstü\\bitirme\\my_model3\\my_model.pt"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model dosyası bulunamadı: {MODEL_PATH}")

model = YOLO(MODEL_PATH)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Sınıf adlarını yükle
CLASS_NAMES = ['glass', 'metal', 'paper', 'plastic']

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Dosya bulunamadı"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Dosya seçilmedi"}), 400

    
    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

 
    results = model(filepath)

 
    detections = []
    class_counts = {}  
    for result in results:
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

    return jsonify({"detections": detections, "class_counts": class_counts})  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)