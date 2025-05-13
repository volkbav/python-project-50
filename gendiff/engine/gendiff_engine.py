import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')

    parser.add_argument(
        '-f', '--format',
        help='set format of output',
    )
    
    return parser.parse_args()


def parse_json(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
        return content
    
def gendiff():
    args = parse_args()
    print(args)
#    print(ARGS.first_file)
#    print(ARGS.second_file)
    first_file_content = parse_json(args.first_file)
    second_file_content = parse_json(args.second_file)
    print(f'file1: \n {first_file_content}')
    print(f'file2: \n {second_file_content}')
