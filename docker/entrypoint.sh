#!/bin/bash
set -e

echo "Checking for missing packages from requirements.txt..."
pip install -r requirements.txt

# Execute the command passed to the container
exec "$@" 