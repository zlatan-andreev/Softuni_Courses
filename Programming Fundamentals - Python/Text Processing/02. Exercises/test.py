text = input()

for i in text:
    if not i.isalnum():
        print("alnum")
    else:
        print("not alnum")