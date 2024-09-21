def add_underscores_to_title(title: str) -> str:
    code_number, code_title = title.split('.')
    return '{code_title}_{code_number}'.format(
        code_title='_'.join(code_title.split(' ')).lstrip('_'),
        code_number=code_number
    )


print(add_underscores_to_title(''))