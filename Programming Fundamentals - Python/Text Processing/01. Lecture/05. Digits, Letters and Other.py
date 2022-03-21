text = input()
digits = ""
letters = ""
others = ""

for i in text:
    if i.isdigit():
        digits += i
    elif i.islower() or i.isupper():
        letters += i
    else:
        others += i
print(digits)
print(letters)
print(others)