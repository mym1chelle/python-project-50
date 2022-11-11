import sys

sys.path.append('gendiff')


from gendiff_func.generate_differece import generate_diff


result_file = open('tests/fixtures/comparison_result.txt', 'r').read()


def test_correct_work_gendiff():
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json')
    assert result == result_file
