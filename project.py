import json
import yaml
import xml.etree.ElementTree as ET
import os
import sys

class FileChanger:
    def load_file(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Blad w odczycie pliku: {e}")
            return ""

    def save_file(self, file_path: str, content: str) -> bool:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Blad w zapisie pliku: {e}")
            return False

def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1][1:].lower()

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_ext = get_file_extension(input_file)
    output_ext = get_file_extension(output_file)


    valid_extensions = ['json', 'yaml', 'yml', 'xml']
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        print(f"Program nie obsluguje tego rozszerzenia :(")
        sys.exit(1)

    processor = FileChanger()
    
    # Load content
    content = processor.load_file(input_file)
    if not content:
        print("Nie mozna odczytac pliku")
        sys.exit(1)

    # Save content
    if not processor.save_file(output_file, content):
        print("Nie mozna zapisac do pliku")
        sys.exit(1)


if __name__ == "__main__":
    main()