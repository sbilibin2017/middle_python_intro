'''Генератор приветствий.'''


def greeting(name: str) -> str:
    '''Возвращает текст приветствия.

    :param str name: имя пользователя
    :return str: текст приветствия
    '''
    # разделяем полное имя на имя и фамилию с помощью пробелов
    name_splitted = name.split(' ')
    # имяи фамилия начинаются с заглавных букв
    name_splitted_capitalized = [word.capitalize() for word in name_splitted]
    # склеиваем имяи фамилию в полное имя
    name_prepared = ' '.join(name_splitted_capitalized)

    return f'Привет, {name_prepared}'
