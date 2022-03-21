first_string = input()
second_string = input()

while True:
    a = second_string.replace(first_string,"")
    if first_string not in a:
        break
print(a)