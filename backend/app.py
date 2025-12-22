from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os

from config import UPLOAD_FOLDER, OUTPUT_FOLDER
from processing.pipeline import run_pipeline
from utils.validators import allowed_file

app = Flask(__name__)
CORS(app)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/enhance", methods=["POST"])
def enhance():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, file.filename)

    file.save(input_path)
    run_pipeline(input_path, output_path)

    return send_file(output_path, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)

