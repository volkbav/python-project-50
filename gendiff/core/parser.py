import json

def parse(file_path):
    return parse_json(file_path)


def parse_json(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
        return content


