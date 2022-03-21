text = input().split(", ")
results = []
flag = False
underscore_counter = 0
hyphen_counter = 0

for word in text:
    flag = False
    underscore_counter = 0
    hyphen_counter = 0

    if not 2 < len(word) < 17:
        flag = True

    for i in word:
        if not i.isalnum() and i!= "-" and i != "_":
            flag = True

    for i in word:
        if i == "_":
            underscore_counter+=1
        if i == "-":
            hyphen_counter +=1
    if underscore_counter >1 or hyphen_counter >1:
        flag = True



    if not flag:
        results.append(word)

for i in results:
    print(i)
