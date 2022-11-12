import json
from yaml import load, Loader
from gendiff.files_parser import parser_file


def generate_diff(file_path1, file_path2):
    if file_path1.endswith('json') and file_path2.endswith('json'):
        return parser_file(json.load(open(file_path1)),
                           json.load(open(file_path2)))
    else:
        return parser_file(load(open(file_path1), Loader=Loader),
                           load(open(file_path2), Loader=Loader))
