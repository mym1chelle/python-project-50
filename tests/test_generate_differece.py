import sys

sys.path.append('gendiff')


from gendiff_func.generate_differece import generate_diff


result_file = open('tests/fixtures/comparison_result.txt', 'r').read()


def test_gendiff_json():
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json')
    assert result == result_file


def test_gendiff_yml():
    result = generate_diff('tests/fixtures/file1.yml',
                           'tests/fixtures/file2.yml')
    assert result == result_file


def test_gendiff_yaml():
    result = generate_diff('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml')
    assert result == result_file
