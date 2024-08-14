from fastapi import FastAPI, UploadFile, File
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = FastAPI()

# Load the trained model
model = load_model("/app/models/land_cover_model.h5")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file)
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)
    return {"predicted_class": int(predicted_class)}
