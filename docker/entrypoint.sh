#!/bin/bash
set -e

echo "Checking for missing packages from requirements.txt..."
pip install -r requirements.txt

echo "Installing Jupyter kernel..."
python -m ipykernel install --user --name jupyter-container --display-name "Jupyter Container"
echo "Jupyter kernel installed successfully!"

# Execute the command passed to the container
exec "$@" 