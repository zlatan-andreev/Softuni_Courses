text = input()
while text != "end":

    a = reversed(text)
    a = "".join(a)
    print(f"{text} = {a}")

    text = input()