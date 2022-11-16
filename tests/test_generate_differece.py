from gendiff.gendiff_func.generate_differece import generate_diff


result_stylish = open('tests/fixtures/result_stylish.txt').read()
result_plain = open('tests/fixtures/result_plain.txt').read()


def test_gendiff_stylish_structure_json():
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json')
    assert result == result_stylish


def test_gendiff_stylish_structure_yml():
    result = generate_diff('tests/fixtures/file1.yml',
                           'tests/fixtures/file2.yml')
    assert result == result_stylish


def test_gendiff_stylish_structure_yaml():
    result = generate_diff('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml')
    assert result == result_stylish


def test_gendiff_plain_structure_json():
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json',
                           'plain')
    assert result == result_plain


def test_gendiff_plain_structure_yml():
    result = generate_diff('tests/fixtures/file1.yml',
                           'tests/fixtures/file2.yml',
                           'plain')
    assert result == result_plain


def test_gendiff_plain_structure_yaml():
    result = generate_diff('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml',
                           'plain')
    assert result == result_plain
