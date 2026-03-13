#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Check if data.json exists
if [ ! -f "data.json" ]; then
    echo "Error: data.json not found!"
    echo "Please generate data.json by running: python ./generate_data.py"
    exit 1
fi

echo "Starting Equito Dashboard server..."
echo "Dashboard available at http://localhost:5050"
echo "Press CTRM-C to stop"
echo ""

python ./server.py
