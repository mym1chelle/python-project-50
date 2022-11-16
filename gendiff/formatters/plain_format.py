import itertools

STATUS = ['added', 'removed', 'changed']


def convert_value(key_value):
    if isinstance(key_value, dict):
        return "[complex value]"
    elif isinstance(key_value, bool):
        return "true" if key_value else "false"
    elif key_value is None:
        return "null"
    elif isinstance(key_value, int):
        return str(key_value)
    else:
        return f"'{str(key_value)}'"


def create_string(path_to_change, key, value):
    end_path = path_to_change + f'{key}'
    if type(value) == dict and value.get('status') in ['added', 'removed']:
        v = convert_value(value['value'])
        if value.get('status') == 'added':
            property_str = f"Property '{end_path}' was added with value: {v}"
        else:
            property_str = f"Property '{end_path}' was removed"
    elif type(value) == dict and value.get('status') == 'changed':
        v_old = convert_value(value['old_value'])
        v_new = convert_value(value['new_value'])
        end_path = path_to_change + f'{key}'
        property_str = f"Property '{end_path}' was updated.\
 From {v_old} to {v_new}"
    return property_str


def plain(area):
    def walk(node, node_key='', path_to_change=''):
        if node_key != '':
            path_to_change += str(node_key) + '.'
        result_list = []
        for key, value in node.items():
            if type(value) == dict and value.get('status') == 'children':
                v = value['value']
                result_list.append(
                    f'''{walk(
                            node=v,
                            node_key=key,
                            path_to_change=path_to_change)}'''
                )
            elif type(value) == dict and value.get('status') in STATUS:
                result_list.append(create_string(path_to_change, key, value))
        result = itertools.chain(result_list)
        return '\n'.join(result)
    return walk(area)
