import itertools
import os


def case_change(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


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
                            'value': case_change(one_dict[key])}
    for key in add_keys:
        result_dict[key] = {'status': 'added',
                            'value': case_change(two_dict[key])}
    for key in shared_keys:
        one = one_dict[key]
        two = two_dict[key]
        if type(one) == dict and type(two) == dict:
            result_dict[key] = get_diff(one, two)
        elif one == two:
            result_dict[key] = {'status': 'unchanged',
                                'value': case_change(one)}
        else:
            result_dict[key] = {'status': 'changed',
                                'old_value': case_change(one),
                                'new_value': case_change(two)}
    return dict(sorted(result_dict.items()))


def stylish(area, replacer='  '):
    def walk(value, length):
        if type(value) != dict:
            return str(value)
        tab = replacer * length
        tab_ = replacer * (length - 1)
        lines = []
        STATUS = {
            'unchanged': "  ",
            'added': "+ ",
            'removed': "- "
        }
        for key, val in value.items():
            if type(val) == dict and val.get('status') == 'changed':
                v_old = val['old_value']
                v_new = val['new_value']
                lines.append(f'{tab}- {key}: {walk(v_old, length + 2)}')
                lines.append(f'{tab}+ {key}: {walk(v_new, length + 2)}')
            elif type(val) == dict and val.get('status') in STATUS.keys():
                v = val['value']
                status = STATUS[val['status']]
                lines.append(f'{tab}{status}{key}: {walk(v, length + 2)}')
            else:
                lines.append(f'{tab}  {key}: {walk(val, length + 2)}')
        result = itertools.chain("{", lines, [tab_ + "}"])
        return '\n'.join(result)
    return walk(area, 1)


FORMATTERS = {
    'stylish': stylish
}
