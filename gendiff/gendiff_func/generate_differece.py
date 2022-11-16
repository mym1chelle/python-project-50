import json
from yaml import safe_load
from gendiff.gendiff_func.dict_parser import get_diff, get_file_format
from gendiff.gendiff_func.dict_parser import FORMATTERS

available_formats = {
    'json': json.load,
    'yaml': safe_load,
    'yml': safe_load
}


def files_reader(data, extension):
    if extension not in available_formats:
        raise TypeError('Unsupported format. Next formats are supported: {}'
                        .format(available_formats.keys()))
    return available_formats[extension](data)


def generate_diff(file_path1, file_path2, format='stylish'):
    file_one = files_reader(open(file_path1), get_file_format(file_path1))
    file_two = files_reader(open(file_path2), get_file_format(file_path2))
    diff = get_diff(file_one, file_two)
    return FORMATTERS[format](diff)
