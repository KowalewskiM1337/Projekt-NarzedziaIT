import json
import yaml
import xml.etree.ElementTree as ET
from typing import Dict, Any
import os
import sys

class FileProcessor:
    def __init__(self):
        self.data = {}

    def load_json(self, file_path: str) -> bool:
        """Load and validate JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            return True
        except json.JSONDecodeError as e:
            print(f"JSON syntax error: {e}")
            return False
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return False

    def save_json(self, file_path: str) -> bool:
        """Save data to JSON file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving JSON file: {e}")
            return False