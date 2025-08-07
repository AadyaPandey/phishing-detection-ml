#!/usr/bin/env bash

echo "Installing Python and required packages..."

# Update and install Python 3 & pip
apt-get update && apt-get install -y python3 python3-pip

# Install Python packages
pip3 install -r requirements.txt

echo "Python setup complete."
