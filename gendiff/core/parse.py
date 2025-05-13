import json


def parse_json(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
        return content

