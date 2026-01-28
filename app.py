from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import base64, io

app = Flask(__name__)
model = tf.keras.models.load_model("model.h5")

def preprocess(image):
    image = image.convert("L")              # grayscale
    image = image.resize((28, 28))           # resize
    image = ImageOps.invert(image)           # invert colors
    image = np.array(image).astype("float32")
    image = image / 255.0                    # normalize
    image = image.reshape(1, 28, 28, 1)      # reshape for CNN
    return image

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_draw", methods=["POST"])
def predict_draw():
    data = request.json["image"]
    image_data = base64.b64decode(data.split(",")[1])
    image = Image.open(io.BytesIO(image_data))

    image = preprocess(image)
    prediction = model.predict(image)
    digit = int(np.argmax(prediction))

    return jsonify({"prediction": digit})

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    image = Image.open(file)

    image = preprocess(image)
    prediction = model.predict(image)
    digit = int(np.argmax(prediction))

    return render_template("index.html", upload_result=digit)

if __name__ == "__main__":
    app.run(debug=True)
