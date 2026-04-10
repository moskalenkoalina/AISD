BRACKETS = {
    "(": ")",
    "[": "]",
    "{": "}"
}

def check(sequence: str):
    stack = []

    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False

            opening = stack.pop()
            if BRACKETS[opening] != bracket:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    sequence = input().strip()

    if check(sequence):
        print("yes")
    else:
        print("no")