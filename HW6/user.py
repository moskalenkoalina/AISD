
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
SIZE = 200003

table = []
DELETED = object()


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global table
    table = [None] * SIZE
    return


def _hash(key):
    """ Проста хеш-функція для рядка """
    h = 0
    for ch in key:
        h = (h * 31 + ord(ch)) % SIZE
    return h


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global table
    index = _hash(author)

    first_deleted = -1  # запам’ятовуємо перший DELETED

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            # якщо знайшли порожню клітинку
            if first_deleted != -1:
                table[first_deleted] = (author, {title})
            else:
                table[pos] = (author, {title})
            return

        if table[pos] is DELETED:
            if first_deleted == -1:
                first_deleted = pos
            continue

        stored_author, books = table[pos]

        if stored_author == author:
            books.add(title)
            return


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """

    """ Перевіряє чи міститься задана книга у бібліотеці. """
    global table
    index = _hash(author)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            return False

        if table[pos] is DELETED:
            continue

        stored_author, books = table[pos]

        if stored_author == author:
            return title in books

    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    """ Видаляє книгу з бібліотеки. """
    global table
    index = _hash(author)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            return

        if table[pos] is DELETED:
            continue

        stored_author, books = table[pos]

        if stored_author == author:
            if title in books:
                books.remove(title)

                # якщо в автора більше немає книг — видаляємо автора
                if len(books) == 0:
                    table[pos] = DELETED
            return


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    """ Повертає список книг заданого автора у алфавітному порядку. """
    global table
    index = _hash(author)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            return []

        if table[pos] is DELETED:
            continue

        stored_author, books = table[pos]

        if stored_author == author:
            return sorted(list(books))
    return []

