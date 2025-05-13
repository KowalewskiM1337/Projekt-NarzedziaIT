import json
import yaml
import xml.etree.ElementTree as ET
from typing import Dict, Any
import os
import sys

class FileChanger:
    def __init__(self):
        self.data = {}

    def load_json(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            return True
        except json.JSONDecodeError as e:
            print(f"Blad skladni: {e}")
            return False
        except Exception as e:
            print(f"Blad w odczycie pliku: {e}")
            return False

    def save_json(self, file_path: str) -> bool:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4)
            return True
        except Exception as e:
            print(f"Blad w zapisie pliku: {e}")
            return False

    def load_yaml(self, file_path: str) -> bool:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.data = yaml.safe_load(file)
                return True
            except yaml.YAMLError as e:
                print(f"Blad skladni: {e}")
                return False
            except Exception as e:
                print(f"Blad w odczycie pliku: {e}")
                return False
            
    def save_yaml(self, file_path: str) -> bool:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                yaml.dump(self.data, file, default_flow_style=False)
            return True
        except Exception as e:
            print(f"Blad w zapisie pliku: {e}")
            return False
        
    def load_xml(self, file_path: str) -> bool:
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            self.data = self._xml_to_dict(root)
            return True
        except ET.ParseError as e:
            print(f"Blad skladni: {e}")
            return False
        except Exception as e:
            print(f"Blad w odczycie pliku: {e}")
            return False
    
    def save_xml(self, file_path: str) -> bool:
        try:
            root = self._dict_to_xml(self.data)
            tree = ET.ElementTree(root)
            tree.write(file_path, encoding='utf-8', xml_declaration=True)
            return True
        except Exception as e:
            print(f"Blad w zapisie pliku: {e}")
            return False