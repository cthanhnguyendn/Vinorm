#!/bin/bash

echo "=== Building Simple Windows Version (without ICU) ==="

# Navigate to the project directory
cd /mnt/e/project/github/Vinorm/cpp_src/src

# Build a simple version without ICU
echo "Building simple version without ICU..."

x86_64-w64-mingw32-g++ -std=c++11 -o main.exe \
    main.cpp \
    ICUReadFile.cpp \
    ICUMapping.cpp \
    ICUNumberConverting.cpp \
    ICUDictionary.cpp \
    SpecialCase.cpp \
    Address.cpp \
    Math.cpp \
    DateTime.cpp \
    -I../include \
    -DNO_ICU \
    -static-libgcc -static-libstdc++ \
    -static

if [ $? -eq 0 ]; then
    echo "✓ Windows build successful!"
    
    # Copy to main directory
    cp main.exe ../../vinorm/
    echo "✓ Copied main.exe to vinorm/"
    
    # Check file size
    ls -la main.exe
    echo "✓ Windows executable created successfully!"
    
else
    echo "✗ Windows build failed!"
    exit 1
fi 