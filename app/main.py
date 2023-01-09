'''Генератор приветствий.'''


def greeting(name: str) -> str:
    '''Возвращает текст приветствия.

    :param str name: имя пользователя
    :return str: текст приветствия
    '''
    # извлекаем слова из имени
    words = name.split(' ')
    # каждое слово начинается с заглавной буквы
    words_capitalized = [word.capitalize() for word in words]
    # склеиваем слова
    name_prepared = ' '.join(words_capitalized)

    return f'Привет, {name_prepared}'
