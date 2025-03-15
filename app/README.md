# App 

This directory contains the core application code for the machine learning API service. The application is built using FastAPI, a modern web framework for building APIs with Python. It serves as the backend for making predictions using our trained machine learning model.

The application follows a modular structure where:
- The API endpoints handle incoming requests for predictions
- The machine learning model is loaded and used for making predictions
- Input validation ensures data consistency
- Logging provides operational visibility

The code is organized to be maintainable, scalable, and follows Python best practices for package structure.

- $\textcolor{#FF4500}{\text{You can easily adapt the repository to work with any dataset of your choice.}}$   
- The structure is flexible and can be applied to various machine learning models, including $\textcolor{#1E90FF}{\text{regression, classification, and clustering}}$.      
&nbsp;   

# `__init__.py`

This file marks the `app` directory as a Python package. It includes:

- **`__all__`**: Specifies the modules available for import when using `from app import *`. Currently, it includes `main`.
- **`VERSION`**: A version identifier for the package, set to '1.0.0'.
- **Imports**: The `predict` function from `main.py` is imported to make it available at the package level.

This file is currently minimal but can be expanded to initialize important variables or import key functions for package-level access.

# `main.py`

This file contains the main application logic for a FastAPI-based web service. Key components include:

- **Logging Setup**: Configures logging to provide debug and error information.
- **FastAPI Application**: Initializes a FastAPI app instance.
- **Model Loading**: Loads a machine learning model from a specified path (`models/ml_model.pkl`). Logs success or error messages during the loading process.
- **Data Model**: Defines an `ModelInput` class using Pydantic for input validation. It includes features of the dataset: `sepal_length`, `sepal_width`, `petal_length`, and `petal_width`.
- **Endpoints**:
  - **Root (`/`)**: A simple GET endpoint to check the API status.
  - **Predict (`/predict`)**: A POST endpoint that accepts flower measurements, makes a prediction using the loaded model, and returns the predicted class along with the input features.
- **Running the App**: If executed as the main module, the app runs using Uvicorn on host `0.0.0.0` and port `8000`.

This file is the core of the application, handling both the API logic and the machine learning model integration.
