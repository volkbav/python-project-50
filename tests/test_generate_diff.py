from gendiff import generate_diff

def test_step3():
    first_file_content, second_file_content = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
        )
    print(
        f'\n---test_step3---\n'
        f'file1: \n {first_file_content}\n',
        f'file2: \n {second_file_content}\n',
        '---test_step3---\n'
          )

