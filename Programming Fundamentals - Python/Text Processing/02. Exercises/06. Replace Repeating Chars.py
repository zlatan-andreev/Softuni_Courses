text = input()
result = ''

for i in range(len(text)-1):
    letter = text[i]
    if letter != text[i+1]:
        result += letter

print(result+text[-1])