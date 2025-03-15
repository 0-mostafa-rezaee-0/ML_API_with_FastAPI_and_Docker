# Docker

This directory contains Dockerfiles for setting up and running different components of the project in isolated environments. Docker allows for consistent and reproducible environments, making it easier to deploy and manage applications.

## Contents

- **`Dockerfile.api`**: This Dockerfile is used to build a Docker image for running the FastAPI application. It includes:
  - **Base Image**: Uses `python:3.10-slim` as the base image for a lightweight Python environment.
  - **Dependencies**: Installs required Python packages from `requirements.txt`.
  - **Application Code**: Copies the application code into the Docker image.
  - **Port Exposure**: Exposes port 8000 for the FastAPI application.
  - **Command**: Runs the FastAPI application using Uvicorn.

- **`Dockerfile.jupyter`**: This Dockerfile is used to build a Docker image for running Jupyter Notebook and JupyterLab. It includes:
  - **Base Image**: Uses a Python version specified by the `PYTHON_VERSION` argument for flexibility.
  - **Dependencies**: Installs required Python packages from `requirements.txt` and additional packages for Jupyter.
  - **Application Code**: Copies the application code into the Docker image.
  - **Port Exposure**: Exposes port 8888 for Jupyter Notebook.
  - **Command**: Runs Jupyter Notebook, allowing access without a token for ease of use.

## Usage

To build and run the Docker images, navigate to the root of the project and use the following commands:

### Build and Run FastAPI

```bash
docker build -t my-fastapi-app -f docker/Dockerfile.api .
docker run -p 8000:8000 my-fastapi-app
```

### Build and Run Jupyter Notebook

```bash
docker build --build-arg PYTHON_VERSION=3.10 -t my-jupyter-notebook -f docker/Dockerfile.jupyter .
docker run -p 8888:8888 my-jupyter-notebook
```

These Dockerfiles provide a convenient way to set up and run the project's components in isolated environments, ensuring consistency across different development and production setups.
