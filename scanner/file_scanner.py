# scanner/file_scanner.py
import os
from pathlib import Path

def scan_directory(directory: str, extensions: list = None):
    """Recursively scans the directory and returns file paths (filtered by extensions if given)"""
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if extensions:
                if any(file.endswith(ext) for ext in extensions):
                    file_list.append(os.path.join(root, file))
            else:
                file_list.append(os.path.join(root, file))
    return file_list
