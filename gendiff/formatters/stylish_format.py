import itertools


STATUS = {
    'children': "  ",
    'unchanged': "  ",
    'added': "+ ",
    'removed': "- "
}


def case_change(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def create_tree(val):
    v = case_change(val['value'])
    if type(v) == dict:
        v = val['value']
    status = STATUS[val['status']]
    return v, status


def stylish(area, replacer='  '):
    def walk(value, length):
        if type(value) != dict:
            return str(value)
        tab = replacer * length
        tab_ = replacer * (length - 1)
        lines = []
        for key, val in value.items():
            if type(val) == dict and val.get('status') == 'changed':
                v_old = case_change(val['old_value'])
                v_new = case_change(val['new_value'])
                lines.append(f'{tab}- {key}: {walk(v_old, length + 2)}')
                lines.append(f'{tab}+ {key}: {walk(v_new, length + 2)}')
            elif type(val) == dict and val.get('status') in STATUS.keys():
                v, status = create_tree(val)
                lines.append(f'{tab}{status}{key}: {walk(v, length + 2)}')
            else:
                lines.append(f'{tab}  {key}: {walk(val, length + 2)}')
        result = itertools.chain("{", lines, [tab_ + "}"])
        return '\n'.join(result)
    return walk(area, 1)
