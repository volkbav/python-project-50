import argparse
import json


def gendiff():
    print(ARGS.first_file)
    print(ARGS.second_file)

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

ARGS = parse_args()

def parse_json(file_path):
    with open(file_path, 'r') as file:
        content = json.loads(file)
        return content
    
def gendiff():
    print(ARGS)
    print(ARGS.first_file)
    print(ARGS.second_file)