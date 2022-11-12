def case_change(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return value


def parser_file(file_one, file_two):
    keys = sorted(file_one.keys() | file_two.keys())
    result = '{\n'
    for key in keys:
        if key not in file_one:
            result += f' + {key}: {case_change(file_two[key])}\n'
        elif key not in file_two:
            result += f' - {key}: {case_change(file_one[key])}\n'
        elif file_one[key] == file_two[key]:
            result += f'   {key}: {case_change(file_one[key])}\n'
        else:
            result += f' - {key}: {case_change(file_one[key])}\n'
            result += f' + {key}: {case_change(file_two[key])}\n'
    result += '}'
    return result
