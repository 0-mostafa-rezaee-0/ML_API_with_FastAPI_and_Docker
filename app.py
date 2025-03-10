from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import logging

# Configure logging before using it
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Log model loading
logging.info("Loading model...")
model = joblib.load("iris_model.pkl")
logging.info("Model loaded successfully.")

# Initialize FastAPI app
app = FastAPI()

# Define input schema using Pydantic
class InputData(BaseModel):
    features: list[float]  # Expecting 4 feature values as a list

# Define API endpoints
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    # Convert input data into NumPy array
    X_input = np.array(data.features).reshape(1, -1)

    # Make prediction
    prediction = model.predict(X_input)[0]
    
    # Log prediction request
    logging.info(f"Received prediction request: {data.features} → Predicted class: {prediction}")

    # Return prediction as JSON
    return {"predicted_class": int(prediction)}
