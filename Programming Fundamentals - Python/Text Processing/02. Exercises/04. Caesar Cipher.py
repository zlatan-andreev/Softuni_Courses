text = input()
result = ''

for i in text:
    position = ord(i)
    new_position = position+3
    new_char = chr(new_position)
    result += new_char

print(result)