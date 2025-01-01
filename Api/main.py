from fastapi import FastAPI,Form,UploadFile
import tensorflow as tf
import numpy as np
import pandas as pd
from pydantic import BaseModel
from PIL import Image
import io

app = FastAPI()

model = tf.keras.models.load_model("./SavedModel/dog_cnn.h5")
dog_labels = pd.read_csv("./labels.csv")

class Item(BaseModel):
    name:str

@app.post("/predict")
async def predict(name:str= Form(...),image:UploadFile = Form(...)):
    file = await image.read()
    def preprocessing_image(file):
        image_depth = Image.open(io.BytesIO(file)).convert("RGB")
        image_resize= image_depth.resize((128,128))
        image_scaled = np.asarray(image_resize)/255
        image_dimenshioned = np.expand_dims(image_scaled,axis=0)
        return image_dimenshioned
    proprocessed_image = preprocessing_image(file)
    prediction = model.predict(proprocessed_image)
    prediction_max = np.argmax(prediction)
    probability = float(prediction[0][prediction_max])
    prediction = np.unique(dog_labels.breed)[prediction_max]
    return {"Predicted Breed":prediction,"probability":probability}
