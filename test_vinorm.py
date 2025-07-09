#!/usr/bin/env python3
"""
Test script for Vinorm Vietnamese text normalization
"""

import sys
import os
from vinorm import TTSnorm

def test_basic_functionality():
    """Test basic text normalization"""
    print("=== Testing Basic Functionality ===")
    
    test_cases = [
        "Hàm này được phát triển từ 8/2019.",
        "Có phải tháng 12/2020 đã có vaccine phòng ngừa Covid-19?",
        "Số điện thoại: 0123456789",
        "Email: test@example.com",
        "Website: https://www.example.com",
        "Số tiền: 1,000,000 VND",
        "Ngày: 25/12/2023",
        "WTO và UNESCO là các tổ chức quốc tế"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\nTest {i}:")
        print(f"Input: {text}")
        try:
            result = TTSnorm(text)
            print(f"Output: {result}")
        except Exception as e:
            print(f"Error: {e}")

def test_parameters():
    """Test different parameter combinations"""
    print("\n=== Testing Parameters ===")
    
    test_text = "Hàm này được phát triển từ 8/2019. WTO và UNESCO!"
    
    # Test with different parameter combinations
    params = [
        {"punc": False, "unknown": True, "lower": True, "rule": False},
        {"punc": True, "unknown": True, "lower": True, "rule": False},
        {"punc": False, "unknown": True, "lower": False, "rule": False},
        {"punc": False, "unknown": True, "lower": True, "rule": True},
    ]
    
    for i, param in enumerate(params, 1):
        print(f"\nParameter Test {i}: {param}")
        try:
            result = TTSnorm(test_text, **param)
            print(f"Output: {result}")
        except Exception as e:
            print(f"Error: {e}")

def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n=== Testing Edge Cases ===")
    
    edge_cases = [
        "",  # Empty string
        "   ",  # Whitespace only
        "1234567890",  # Numbers only
        "!@#$%^&*()",  # Special characters only
        "A" * 1000,  # Very long string
        "Tiếng Việt có dấu: á à ả ã ạ ă ắ ằ ẳ ẵ ặ â ấ ầ ẩ ẫ ậ",  # Vietnamese diacritics
    ]
    
    for i, text in enumerate(edge_cases, 1):
        print(f"\nEdge Case {i}:")
        print(f"Input: {repr(text)}")
        try:
            result = TTSnorm(text)
            print(f"Output: {result}")
        except Exception as e:
            print(f"Error: {e}")

def test_file_operations():
    """Test if the package can handle file operations correctly"""
    print("\n=== Testing File Operations ===")
    
    # Check if required files exist
    required_files = [
        "vinorm/main",
        "vinorm/input.txt",
        "vinorm/output.txt"
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} missing")

def main():
    """Run all tests"""
    print("Vinorm Test Suite")
    print("=" * 50)
    
    try:
        test_file_operations()
        test_basic_functionality()
        test_parameters()
        test_edge_cases()
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        
    except Exception as e:
        print(f"\nTest suite failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 