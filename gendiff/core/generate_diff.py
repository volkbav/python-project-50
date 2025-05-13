from gendiff.core.parse import parse_json

def generate_diff(file_path1, file_path2, format=None):
    first_file_content = parse_json(file_path1)
    second_file_content = parse_json(file_path2)
    print(f'file1: \n {first_file_content}')
    print(f'file2: \n {second_file_content}')
    return first_file_content, second_file_content
