import os

from gendiff import generate_diff


def test_generate_diff():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path1 = os.path.join(current_dir, 'test_data', 'file1.json')
    file_path2 = os.path.join(current_dir, 'test_data', 'file2.json')
    with open(os.path.join(
        current_dir, 'test_data', 'expected1_2.txt'), 'r'
        ) as file:
        expected_result = file.read()
    result = generate_diff(file_path1, file_path2)

    assert result == expected_result
    