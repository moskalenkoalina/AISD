SIZE = 20011
table = [None] * SIZE

def hash_function(word):
    h = 0
    i = 0
    while i < len(word):
        h = (h * 31 + ord(word[i])) % SIZE
        i += 1
    return h

def insert(word):
    index = hash_function(word)

    while table[index] is not None:
        if table[index][0] == word:
            return
        index = (index + 1) % SIZE

    table[index] = [word, False]

def find(word):
    index = hash_function(word)

    while table[index] is not None:
        if table[index][0] == word:
            return index
        index = (index + 1) % SIZE

    return -1

n, m = map(int, input().split())


for _ in range(n):
    w = input().strip().lower()
    insert(w)

text = ""
for _ in range(m):
    text += input() + " "

words = []
current = ""

i = 0
while i < len(text):
    ch = text[i]

    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
        current += ch
    else:
        if current != "":
            words.append(current)
            current = ""
    i += 1

if current != "":
    words.append(current)

unknown = False

i = 0
while i < len(words):
    pos = find(words[i])
    if pos == -1:
        unknown = True
        break
    table[pos][1] = True
    i += 1

if unknown:
    print("Some words from the text are unknown.")
else:
    i = 0
    while i < SIZE:
        if table[i] is not None and table[i][1] == False:
            print("The usage of the vocabulary is not perfect.")
            break
        i += 1
    else:
        print("Everything is going to be OK.")