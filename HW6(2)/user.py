
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
SIZE = 100003  # розмір хеш-таблиці

table = []


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global table
    table = [[] for _ in range(SIZE)]


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

    chain = table[index]

    # шукаємо автора в ланцюжку
    for i in range(len(chain)):
        stored_author, books = chain[i]
        if stored_author == author:
            books.add(title)
            return

    # якщо автора нема — додаємо нового
    chain.append((author, {title}))


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """

    """ Перевіряє чи міститься задана книга у бібліотеці. """
    global table
    index = _hash(author)

    chain = table[index]

    for stored_author, books in chain:
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

    chain = table[index]

    for i in range(len(chain)):
        stored_author, books = chain[i]

        if stored_author == author:
            if title in books:
                books.remove(title)

                # якщо книг більше немає — видаляємо автора
                if len(books) == 0:
                    chain.pop(i)
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

    chain = table[index]

    for stored_author, books in chain:
        if stored_author == author:
            return sorted(list(books))

    return []