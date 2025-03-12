<img src="assets/logo.png" alt="ML API with FastAPI and Docker" width="80%">

# ML API with FastAPI and Docker

***Table of Contents***
<details>
  <summary><a href="#1-about-this-repository"><i><b>1. About this Repository</b></i></a></summary>
  <div>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#11-who-is-this-project-for">1.1. Who Is This Project For?</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#12-what-will-you-learn">1.2. What Will You Learn?</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#13-prerequisites">1.3. Prerequisites</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#14-contents-of-this-repository">1.4. Contents of this Repository</a><br>
  </div>
</details>
&nbsp;

<details>
  <summary><a href="#2-project-structure"><i><b>2. Project Structure</b></i></a></summary>
  <div>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#21-production-environment-dockerization">2.1. Production Environment (Dockerization)</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#22-machine-learning-components">2.2. Machine Learning Components</a><br>
  </div>
</details>
&nbsp;

<div>
  &nbsp;&nbsp;&nbsp;&nbsp;<a href="#3-project-files-and-folders-overview"><i><b>3. Project Files and Folders Overview</b></i></a>
</div>
&nbsp;

<details>
  <summary><a href="#4-how-to-use-and-test-the-project"><i><b>4. How to Use and Test the Project</b></i></a></summary>
  <div>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#41-build-and-start-the-containers">4.1. Build and Start the Containers</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#42-train-the-model">4.2. Train the Model</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#43-test-the-fastapi-endpoints">4.3. Test the FastAPI Endpoints</a><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#44-use-jupyter-for-development">4.4. Use Jupyter for Development</a><br>
  </div>
</details>
&nbsp;

<div>
  &nbsp;&nbsp;&nbsp;&nbsp;<a href="#5-summary"><i><b>5. Summary</b></i></a>
</div>
&nbsp;

<div>
  &nbsp;&nbsp;&nbsp;&nbsp;<a href="#6-for-additional-questions"><i><b>6. For Additional Questions</b></i></a>
</div>
&nbsp;

# 1. About this Repository
This project demonstrates an end-to-end ML engineering workflow. You can train any machine learning model, serve it using a FastAPI application, and experiment interactively with Jupyter Notebook – all within Docker containers. The project is designed to be reproducible and maintainable.

-  This project currently demonstrates classification with the Iris dataset; however, it can be adapted for various tasks such as regression, clustering, and more.
- The Iris dataset is used in this example, but you can replace it with any dataset of your choice.

## 1.1. Who Is This Project For?
This project is designed for anyone interested in machine learning, API development, or containerization with Docker. Whether you're a student, developer, or data scientist, this resource will guide you through building and deploying a machine learning API using FastAPI and Docker.

## 1.2. What Will You Learn?
By the end of this project, you will:
Develop a foundational understanding of FastAPI and its setup.
- Learn the basics of containerizing applications using Docker.
- Explore how to train and deploy simple machine learning models.
- Work with practical examples to build scalable APIs.
- Gain insights into integrating machine learning models into web services.
This project serves as a well-organized example to help you learn about building ML APIs with FastAPI and Docker.

## 1.3. Prerequisites
This project is suitable for three types of learners:

1. **For those familiar with Docker and FastAPI**: You can dive straight into the deployment phase. The examples and configurations provided will help you enhance your skills and explore best practices in building and deploying APIs.

2. **For those who know Docker but are new to FastAPI**: This project will introduce you to FastAPI, guiding you through building and deploying a simple API. By the end, you'll be ready to integrate more complex models.

3. **For beginners with no prior knowledge of Docker or FastAPI**: This project is designed with you in mind. You'll start with the basics, learning how to set up Docker and FastAPI, and then move on to building and deploying a machine learning model. The repository is well-organized and clear, allowing you to easily tweak it for your needs and learn effectively from practical examples.

## 1.4. Contents of this Repository 

```
Folder PATH listing
.
|   .gitignore              <-- Specifies files to ignore in Git version control
|   LICENSE                 <-- License information for the project
|   docker-compose.yml      <-- Docker Compose configuration
|   README.md               <-- Project overview and instructions
|   .dockerignore           <-- Specifies files to ignore in Docker builds
|   requirements.txt        <-- Lists Python dependencies
|   
+---data                    <-- Directory for storing datasets
|       iris.csv            <-- Example dataset for model training
|       
+---docker                  <-- Contains Docker configuration files
|       Dockerfile.api      <-- Dockerfile for building the API service
|       Dockerfile.jupyter  <-- Dockerfile for setting up Jupyter Notebook
|       
+---scripts                 <-- Contains utility scripts
|       train.py            <-- Script for training models
|       
+---assets                  <-- Contains static assets (images, styles, etc.)
|       logo.png            <-- Project logo image
|       
+---app                     <-- Contains the main application code
|       main.py             <-- Main application logic
|       __init__.py         <-- Initializes the app module
|           
+---models                  <-- Stores trained machine learning models
|       iris_model.pkl      <-- Serialized Iris model
|       
\---notebooks               <-- Jupyter notebooks for experiments and analysis
        train_dev.ipynb     <-- Notebook for training and development
        data_exploration.ipynb  <-- Notebook for data exploration
```

# 2. Project Structure

## 2.1. Production Environment (Dockerization)

- **Dockerfile.api**  
  Dockerfile for building the FastAPI container. It installs the dependencies required for serving the model in a production environment.

- **Dockerfile.jupyter**  
  Dockerfile for building the Jupyter Notebook container. It installs additional dependencies for interactive development and experimentation.

- **docker-compose.yml**  
  Defines two services:
  - `api`: Runs the FastAPI application for production, exposing it on port 8000.
  - `jupyter`: Runs a Jupyter Notebook server for development and model training, accessible on port 8888.

## 2.2. Machine Learning Components

- **requirements.txt**  
  Lists all the Python dependencies, including NumPy, pandas, scikit-learn, FastAPI, and others.

- **train.py**  
  A training script that loads the Iris dataset, trains a logistic regression model, evaluates it, and saves the trained model as `iris_model.pkl`.

- **app/main.py**  
  The FastAPI application that loads `iris_model.pkl` and exposes two endpoints:
  - `/health`: Returns a simple health check.
  - `/predict`: Accepts a JSON payload with features and returns the model's prediction.

# 3. Project Files and Folders Overview

- **app/**  
  Contains the main application code:
  - **main.py:** Main application logic for FastAPI.
  - **__init__.py:** Initializes the app module.

- **assets/**  
  Contains static assets like images and styles.

- **data/**  
  Directory for storing datasets used in the project.

- **docker/**  
  Contains Docker configuration files:
  - **Dockerfile.api:** Builds the FastAPI container.
  - **Dockerfile.jupyter:** Builds the Jupyter Notebook container.

- **models/**  
  Stores trained machine learning models, such as `iris_model.pkl`.

- **notebooks/**  
  Jupyter notebooks for experiments and analysis:
  - **train_dev.ipynb:** Notebook for training and development.
  - **data_exploration.ipynb:** Notebook for data exploration.

- **scripts/**  
  Contains utility scripts, such as:
  - **train.py:** Script for training machine learning models.

- **.dockerignore:**  
  Specifies files and directories to be ignored by Docker during the build process.

- **.gitignore:**  
  Specifies files and directories to be ignored by Git version control.

- **LICENSE:**  
  Contains the license information for the project.

- **README.md:**  
  Provides an overview of the project, including setup instructions and documentation.

- **docker-compose.yml:**  
  Defines services, port mappings, and volume mounting for the FastAPI and Jupyter containers.

- **requirements.txt:**  
  Lists all the Python dependencies required for both model training and serving.

- **tree.txt:**  
  A text representation of the directory structure.

# 4. How to Use and Test the Project

## 4.1. Build and Start the Containers

Open a terminal in the project directory and run:

```bash
docker-compose up --build -d
```

This command builds the images for both FastAPI and Jupyter services and starts them in detached mode.

## 4.2. Train the Model

1. Open a shell in the Jupyter container:

   ```bash
   docker-compose exec jupyter bash
   ```

2. Inside the container, run the training script:

   ```bash
   python scripts/train.py
   ```

   The script will train a logistic regression model on the Iris dataset, log the model's accuracy, and save it as `models/iris_model.pkl` in the shared directory.

## 4.3. Test the FastAPI Endpoints

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

## 4.4. Use Jupyter for Development

Open your browser and navigate to [http://localhost:8888](http://localhost:8888) to use the Jupyter Notebook environment. This environment is ideal for further experimentation and interactive development.

# 5. Summary

- **Development and Production Together:**  
  Train your model in the Jupyter container, then serve predictions using FastAPI in a separate container. Both containers share the same code and model files via Docker volumes.

- **Reproducibility:**  
  Using Docker Compose ensures a consistent and easily configurable environment, allowing for seamless transitions between development and production.

- **Testing:**  
  Verify the application's functionality using the provided endpoints for health checks and predictions, ensuring reliability and performance.

# 6. For Additional Questions

If you have any questions or suggestions, feel free to reach out to [Mostafa Rezaee](https://www.linkedin.com/in/mostafa-rezaee/) at Linkedin. You can also open an issue on the project repository.


