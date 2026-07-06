from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Industrial Predictive Maintenance Engine")
model = joblib.load('models/predictive_model.pkl')
scaler = joblib.load('models/feature_scaler.pkl')

class TelemetryInput(BaseModel):
    sensor_readings: list[float] # Structured list containing 21 standard float arrays

@app.post("/predict")
def predict_remaining_life(data: TelemetryInput):
    raw_features = np.array(data.sensor_readings).reshape(1, -1)
    scaled_features = scaler.transform(raw_features)
    prediction = model.predict(scaled_features)
    return {"predicted_remaining_cycles": float(prediction[0])}
  
