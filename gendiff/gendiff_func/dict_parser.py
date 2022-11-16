import os
from gendiff.formatters.stylish_format import stylish
from gendiff.formatters.plain_format import plain
from gendiff.formatters.json_format import json_format


def get_file_format(pathfile):
    extension = os.path.splitext(pathfile)[1].lstrip('.')
    return extension


def get_diff(one_dict: dict, two_dict: dict):
    result_dict = {}
    remove_keys = set(one_dict.keys()) - set(two_dict.keys())
    add_keys = set(two_dict.keys()) - set(one_dict.keys())
    shared_keys = one_dict.keys() & two_dict.keys()

    for key in remove_keys:
        result_dict[key] = {'status': 'removed',
                            'value': one_dict[key]}
    for key in add_keys:
        result_dict[key] = {'status': 'added',
                            'value': two_dict[key]}
    for key in shared_keys:
        one = one_dict[key]
        two = two_dict[key]
        if type(one) == dict and type(two) == dict:
            result_dict[key] = {'status': 'children',
                                'value': get_diff(one, two)}
        elif one == two:
            result_dict[key] = {'status': 'unchanged',
                                'value': one}
        else:
            result_dict[key] = {'status': 'changed',
                                'old_value': one,
                                'new_value': two}
    return dict(sorted(result_dict.items()))


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format
}
