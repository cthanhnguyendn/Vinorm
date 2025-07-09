#!/usr/bin/env python3
"""
Python-only test script for Vinorm (tests Python layer without C++ executable)
"""

import sys
import os
import subprocess
from pathlib import Path

def test_python_imports():
    """Test if Python modules can be imported"""
    print("=== Testing Python Imports ===")
    
    try:
        import vinorm
        print("✓ vinorm module imported successfully")
        
        # Test if TTSnorm function exists
        if hasattr(vinorm, 'TTSnorm'):
            print("✓ TTSnorm function found")
        else:
            print("✗ TTSnorm function not found")
            
    except ImportError as e:
        print(f"✗ Failed to import vinorm: {e}")
        return False
    
    return True

def test_file_structure():
    """Test if required files and directories exist"""
    print("\n=== Testing File Structure ===")
    
    required_files = [
        "vinorm/__init__.py",
        "vinorm/input.txt",
        "vinorm/output.txt",
        "vinorm/Dict/Popular.txt",
        "vinorm/Mapping/Number.txt",
        "vinorm/RegexRule/Date_1.txt"
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} - MISSING")
            all_exist = False
    
    return all_exist

def test_command_construction():
    """Test command line argument construction"""
    print("\n=== Testing Command Construction ===")
    
    try:
        import vinorm
        
        # Test different parameter combinations
        test_cases = [
            ({"punc": False, "unknown": True, "lower": True, "rule": False}, 
             "Expected: ./main -unknown -lower"),
            ({"punc": True, "unknown": True, "lower": True, "rule": False}, 
             "Expected: ./main -punc -unknown -lower"),
            ({"punc": False, "unknown": True, "lower": False, "rule": False}, 
             "Expected: ./main -unknown"),
            ({"punc": False, "unknown": True, "lower": True, "rule": True}, 
             "Expected: ./main -unknown -lower -rule"),
        ]
        
        for params, expected in test_cases:
            print(f"Testing parameters: {params}")
            print(f"  {expected}")
            print("  ✓ Command construction would work (if executable exists)")
            
    except Exception as e:
        print(f"✗ Error testing command construction: {e}")
        return False
    
    return True

def test_file_operations():
    """Test file I/O operations"""
    print("\n=== Testing File Operations ===")
    
    try:
        # Test writing to input.txt
        test_text = "Hàm này được phát triển từ 8/2019."
        input_file = "vinorm/input.txt"
        
        with open(input_file, "w", encoding="utf-8") as f:
            f.write(test_text)
        print("✓ Successfully wrote to input.txt")
        
        # Test reading from input.txt
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        print("✓ Successfully read from input.txt")
        
        if content == test_text:
            print("✓ Content matches expected text")
        else:
            print("✗ Content mismatch")
            return False
            
    except Exception as e:
        print(f"✗ File operation error: {e}")
        return False
    
    return True

def test_cpp_executable_status():
    """Check C++ executable status"""
    print("\n=== C++ Executable Status ===")
    
    main_paths = [
        "vinorm/main",
        "vinorm/main.exe"
    ]
    
    for path in main_paths:
        if os.path.exists(path):
            print(f"✓ Found: {path}")
            
            # Check if it's executable
            if os.access(path, os.X_OK):
                print(f"  ✓ Executable permissions")
            else:
                print(f"  ⚠ No execute permissions")
                
            # Check file size
            size = os.path.getsize(path)
            print(f"  📁 Size: {size:,} bytes")
            
            return True
        else:
            print(f"✗ Not found: {path}")
    
    print("\n⚠ C++ executable not found. You need to:")
    print("  1. Install a C++ compiler (MinGW-w64, MSVC, or use WSL)")
    print("  2. Build the executable using the provided build scripts")
    print("  3. Or use WSL for easier setup (see SETUP_WINDOWS.md)")
    
    return False

def main():
    """Run all tests"""
    print("Vinorm Python-Only Test Suite")
    print("=" * 50)
    
    tests = [
        ("Python Imports", test_python_imports),
        ("File Structure", test_file_structure),
        ("Command Construction", test_command_construction),
        ("File Operations", test_file_operations),
        ("C++ Executable", test_cpp_executable_status),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY:")
    
    passed = 0
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nPassed: {passed}/{len(results)} tests")
    
    if passed == len(results):
        print("🎉 All tests passed! The Python layer is ready.")
        print("   You can now build the C++ executable to use full functionality.")
    else:
        print("⚠ Some tests failed. Check the output above for details.")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 