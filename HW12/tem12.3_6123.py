def f():
    stack = []

    while True:
        comand = input().split()

        if comand[0] == "push":
            n = int(comand[1])
            stack.append(n)
            print("ok")

        elif comand[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print("error")

        elif comand[0] == "back":
            if stack:
                print(stack[-1])
            else:
                print("error")

        elif comand[0] == "size":
            print(len(stack))

        elif comand[0] == "clear":
            stack.clear()
            print("ok")

        elif comand[0] == "exit":
            print("bye")
            break


if __name__ == "__main__":
    f()