text = input().split(" ")
word = ''
result = ''
for i in text:
    word = i*len(i)
    result += word
print(result)