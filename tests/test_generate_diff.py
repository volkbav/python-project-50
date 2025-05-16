from gendiff import generate_diff


def test_generate_diff():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/expected1_2.txt', 'r') as file:
        expected_result = file.read()
        print(f'\n{expected_result}')
    
    result = generate_diff(file_path1, file_path2)
    print(result)
#    assert result == expected_result
    