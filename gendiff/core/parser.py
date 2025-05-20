import json

import yaml


def parse(file_path):
    ext = file_path.split('.')[-1].lower()
    if ext == 'json':
        return parse_json(file_path)
    elif ext in ('yml', 'yaml'):
        return parse_yaml(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")


def parse_json(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
        return content


def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        content = yaml.safe_load(file)
        return content