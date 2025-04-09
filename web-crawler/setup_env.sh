#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Setting up the virtual environment..."

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Setup complete. Activate the virtual environment using 'source .venv/bin/activate'."
