import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define the model path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(PROJECT_ROOT, 'models', 'ml_model.pkl')

# Load the model
try:
    logger.info(f"Loading model from {model_path}")
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise

class ModelInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
async def root():
    logger.debug("Root endpoint called")
    return {"status": "ok", "message": "API is working"}

@app.get("/health")
async def health():
    logger.debug("Health check endpoint called")
    return {"status": "ok"}

@app.post("/predict")
async def predict(data: ModelInput):
    try:
        # Convert input data to list
        features = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return prediction with more information
        return {
            "status": "success",
            "prediction": int(prediction[0]),
            "input_features": features[0]
        }
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
