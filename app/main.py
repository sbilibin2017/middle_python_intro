'''Генератор приветствий.'''


def greeting(name: str) -> str:
    '''Возвращает текст приветствия.

    :param str name: имя пользователя
    :return str: текст приветствия
    '''
    # получаем имя и фамилию
    name_split = name.split(' ')
    # заглавные буквы
    name_split_capitalized = [word.capitalize() for word in name_split]
    # склеиваем полное имя
    name_prepared = ' '.join(name_split_capitalized)
    return f'Привет, {name_prepared}'
