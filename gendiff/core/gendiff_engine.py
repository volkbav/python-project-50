import json
from cli import parse_args

def parse_json(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
        return content
    
def gendiff():
    args = parse_args()
#    print(args)
#    print(ARGS.first_file)
#    print(ARGS.second_file)

    first_file_content = parse_json(args.first_file)
    second_file_content = parse_json(args.second_file)
    print(f'file1: \n {first_file_content}')
    print(f'file2: \n {second_file_content}')
