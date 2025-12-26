from flask import Flask, render_template, request, send_from_directory
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
# Use absolute path for reference image
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCE_IMAGE = os.path.join(BASE_DIR, "model", "original_pan.jpg")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def preprocess_image(path):
    image = cv2.imread(path)
    if image is None:
        return None
    image = cv2.resize(image, (250, 160))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    score = None
    image_path = None

    if request.method == "POST":
        file = request.files["pan_image"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            image_path = file.filename

            original = preprocess_image(REFERENCE_IMAGE)
            uploaded = preprocess_image(filepath)

            # Error handling for missing or invalid images
            if original is None:
                result = f"ERROR: Reference image not found at {REFERENCE_IMAGE}"
            elif uploaded is None:
                result = "ERROR: Uploaded image is corrupted or invalid"
            else:
                try:
                    score, diff = ssim(original, uploaded, full=True)
                    score = round(score, 4)
                    diff = (diff * 255).astype("uint8")

                    # Threshold logic (from your notebook understanding)
                    if score < 0.85:
                        result = "FAKE / TAMPERED PAN CARD"
                    else:
                        result = "GENUINE PAN CARD"
                except Exception as e:
                    result = f"ERROR: {str(e)}"

    return render_template("index.html", result=result, score=score, image_path=image_path)

@app.route("/uploads/<filename>")
def serve_upload(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
