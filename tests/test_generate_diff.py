import os

import pytest

from gendiff.core.generate_diff import generate_diff


@pytest.mark.parametrize(
    'file1, file2, expected',
    [
        (  # test json
            'test_data/file1.json',
            'test_data/file1.json',
            'test_data/expected_flat.txt'    
        ),
        (  # test yml
            'test_data/file1.yml',
            'test_data/file1.yml',
            'test_data/expected_flat.txt'    
        ),
        (  # test yaml
            'test_data/file1.yaml',
            'test_data/file1.yaml',
            'test_data/expected_flat.txt'    
        )
    ]
)
def test_generate_diff(file1, file2, expected):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path1 = os.path.join(current_dir, file1)
    path2 = os.path.join(current_dir, file2)
    expected_path = os.path.join(current_dir, expected)
    with open(expected_path, 'r') as file:
        expected_result = file.read().strip()
    result = generate_diff(path1, path2).strip()

    assert result == expected_result
    