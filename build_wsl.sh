#!/bin/bash

echo "=== Building Vinorm in WSL ==="

# Update package list
echo "Updating package list..."
sudo apt update

# Install required packages
echo "Installing required packages..."
sudo apt install -y git python3 python3-pip python3-venv g++ make

# Navigate to the project directory (Windows path mounted in WSL)
echo "Navigating to project directory..."
cd /mnt/e/project/github/Vinorm

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo "Error: setup.py not found. Make sure you're in the Vinorm project directory."
    exit 1
fi

echo "✓ Found Vinorm project directory"

# Set up Python virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv_wsl
source venv_wsl/bin/activate
pip install -e .

# Build the C++ executable
echo "Building C++ executable..."
cd cpp_src/src

# Set library path for ICU
export LD_LIBRARY_PATH=../lib

# Build using make
echo "Running make..."
make main

if [ $? -eq 0 ]; then
    echo "✓ C++ build successful!"
    
    # Copy the executable to the main vinorm directory
    cp main ../../vinorm/
    echo "✓ Copied main executable to vinorm/"
    
    # Make it executable
    chmod +x ../../vinorm/main
    
    # Go back to project root
    cd ../..
    
    # Test the build
    echo "Testing the build..."
    python test_vinorm.py
    
    echo ""
    echo "=== Build Complete! ==="
    echo "✓ C++ executable built successfully"
    echo "✓ Python package installed"
    echo "✓ Ready to use on Windows!"
    echo ""
    echo "You can now exit WSL and use the application in Windows:"
    echo "  python test_vinorm.py"
    echo "  from vinorm import TTSnorm"
    
else
    echo "✗ C++ build failed!"
    echo "Check the error messages above."
    exit 1
fi 