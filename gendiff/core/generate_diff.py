from gendiff.core.parse import parse_json

def generate_diff(file_path1, file_path2, format=None):
    first_file_content = parse_json(file_path1)
    second_file_content = parse_json(file_path2)
    return first_file_content, second_file_content

