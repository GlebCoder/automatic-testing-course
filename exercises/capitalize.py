def capitalize(argument):
    if argument:
        first_part = argument[0].upper()
        second_part = argument[1:]
        return f'{first_part}{second_part}'
    return ''
