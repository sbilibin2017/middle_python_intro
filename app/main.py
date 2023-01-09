'''Генератор приветствий.'''


def greeting(name: str) -> str:
    '''Возвращает текст приветствия.

    :param str name: имя пользователя
    :return str: текст приветствия
    '''
    name_prepared = ' '.join([word.capitalize() for word in name.split(' ')])

    return f'Привет, {name_prepared}'
