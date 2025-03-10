# p1-ml-engineering-api-fastapi-docker
 Project 1 | ML Engineering best practices  | ML model deployment as a FastAPI service, containerized with Docker for scalability and reproducibility.

 Below is a complete README.md file for your project:

---

# ML Engineering Practice with FastAPI and Jupyter

This project demonstrates an end-to-end ML engineering workflow. You can train a machine learning model, serve it using a FastAPI application, and experiment interactively with Jupyter Notebook – all within Docker containers. The project is designed to be reproducible and maintainable.

---

## Project Structure

- **.env**  
  Contains environment variables. Here, it sets the Python version used for building the images (e.g., `PYTHON_VERSION=3.10`).  
- **Dockerfile.api**  
  Dockerfile for building the FastAPI container. It uses the PYTHON_VERSION from the .env file and installs only the dependencies required for serving the model.
- **Dockerfile.jupyter**  
  Dockerfile for building the Jupyter Notebook container. It also uses the PYTHON_VERSION and installs additional dependencies for interactive development.
- **docker-compose.yml**  
  Defines two services:
  - `fastapi`: Runs the FastAPI application (production-like environment).
  - `jupyter`: Runs a Jupyter Notebook server for model training and experimentation.
- **requirements.txt**  
  Lists all the Python dependencies such as NumPy, pandas, scikit-learn, FastAPI, and others.
- **train.py**  
  A training script that loads the Iris dataset, trains a logistic regression model, evaluates it, and saves the trained model as `iris_model.pkl`.
- **app.py**  
  The FastAPI application that loads `iris_model.pkl` and exposes two endpoints:
  - `/health`: Returns a simple health check.
  - `/predict`: Accepts a JSON payload with features and returns the model’s prediction.

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## How to Use and Test the Project

### Step 1: Build and Start the Containers

Open a terminal in the project directory and run:

```bash
docker-compose up --build -d
```

This command builds the images for both FastAPI and Jupyter services and starts them in detached mode.

### Step 2: Train the Model

1. Open a shell in the Jupyter container:

   ```bash
   docker-compose exec jupyter bash
   ```

2. Inside the container, run the training script:

   ```bash
   python train.py
   ```

   The script will train a logistic regression model on the Iris dataset, log the model’s accuracy, and save it as `iris_model.pkl` in the shared directory.

### Step 3: Test the FastAPI Endpoints

1. **Health Check:**  
   Open your browser and go to [http://localhost:8000/health](http://localhost:8000/health). You should see:

   ```json
   {"status": "ok"}
   ```

2. **Prediction Endpoint:**  
   Send a POST request to [http://localhost:8000/predict](http://localhost:8000/predict) with a JSON body. For example, using curl:

   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
   ```

   You should receive a JSON response with the predicted class.

### Step 4: Use Jupyter for Development

Open your browser and navigate to [http://localhost:8888](http://localhost:8888) to use the Jupyter Notebook environment. This environment is ideal for further experimentation and interactive development.

---

## Explanation of Each File

- **.env:**  
  Centralizes configuration. Change the Python version here to update all containers.

- **Dockerfile.api & Dockerfile.jupyter:**  
  Use the ARG `PYTHON_VERSION` (default set to 3.10) from the .env file. They build isolated environments for FastAPI and Jupyter respectively.

- **docker-compose.yml:**  
  Defines services, port mappings, and volume mounting so that all containers share the same project directory.

- **requirements.txt:**  
  Specifies the libraries needed for both model training and serving.

- **train.py:**  
  Contains the code to train and save your machine learning model. Run this first to generate the model file required by the API.

- **app.py:**  
  Loads the trained model and defines API endpoints. It uses logging to record important events (e.g., model loading and prediction requests).

---

## Summary

- **Development and Production Together:**  
  Train your model in the Jupyter container, then serve predictions using FastAPI in a separate container. Both containers share the same code and model file via Docker volumes.
- **Reproducibility:**  
  By using a .env file and Docker Compose, you ensure that the environment is consistent and easily configurable.
- **Testing:**  
  Use the provided endpoints to verify both health and prediction functionalities.

---

Happy coding! If you have any questions or suggestions, feel free to open an issue or contact the project maintainers.


