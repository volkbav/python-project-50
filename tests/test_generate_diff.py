import os

import pytest

from gendiff.core import generate_diff

# from gendiff.core.generate_diff import generate_diff


@pytest.mark.parametrize(
    'file1, file2, expected, format_name',
    [
        (  # flat no format
            'test_data/flat/file1.json',
            'test_data/flat/file2.json',
            'test_data/expected_flat.txt',
            None 
        ),
        (  # flat stylish yml
            'test_data/flat/file1.yml',
            'test_data/flat/file2.yml',
            'test_data/expected_flat.txt',
            'stylish'

        ),
        (  # flat stylish yaml
            'test_data/flat/file1.yaml',
            'test_data/flat/file2.yaml',
            'test_data/expected_flat.txt',
            'stylish'    
        ),
        (  # flat no changes stylish
            'test_data/flat/file1.json',
            'test_data/flat/file1.json',
            'test_data/no_change.txt',
            'stylish' 
            ),
        (  # --stylish json
            'test_data/file1.json',
            'test_data/file2.json',
            'test_data/expected_stylish.txt',
            'stylish' 
            ), 
        (  # stylish yml
            'test_data/file1.yml',
            'test_data/file2.yml',
            'test_data/expected_stylish.txt',
            'stylish' 
            ),
        (  # stylish yaml
            'test_data/file1.yaml',
            'test_data/file2.yaml',
            'test_data/expected_stylish.txt',
            'stylish' 
            ),
        (  # --plain--- json
            'test_data/file1.json',
            'test_data/file2.json',
            'test_data/expected_plain.txt',
            'plain' 
            ), 
        (  # plain yml
            'test_data/file1.yml',
            'test_data/file2.yml',
            'test_data/expected_plain.txt',
            'plain' 
            ),
        (  # plain yaml
            'test_data/file1.yaml',
            'test_data/file2.yaml',
            'test_data/expected_plain.txt',
            'plain' 
            ),
        (  # json
            'test_data/file1.json',
            'test_data/file2.json',
            'test_data/expected_diff.json',
            'json' 
            )
    ]
)
def test_generate_diff(file1, file2, expected, format_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path1 = os.path.join(current_dir, file1)
    path2 = os.path.join(current_dir, file2)
    expected_path = os.path.join(current_dir, expected)
    with open(expected_path, 'r') as file:
        expected_result = file.read()
    result = generate_diff(path1, path2, format_name)

    assert result == expected_result


        
    

