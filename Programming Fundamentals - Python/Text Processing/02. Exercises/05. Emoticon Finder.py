text = input()
result = []

for i in range(len(text)):
    if text[i] == ":" and text[i+1] != " ":
        result.append(text[i]+text[i+1])
for i in result:
    print(i)