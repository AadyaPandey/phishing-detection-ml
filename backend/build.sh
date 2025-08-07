#!/usr/bin/env bash

echo "Installing Python and required packages..."

# Update package lists and install Python 3 & pip
apt-get update && apt-get install -y python3 python3-pip

# Install Python packages from the correct path
pip3 install -r backend/python/requirements.txt
