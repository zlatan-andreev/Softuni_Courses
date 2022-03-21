text = input()

slash_index = text.rfind("\\")
dot_index = text.rfind(".")

print(f'File name: {text[slash_index+1:dot_index]}')
print(f'File extension: {text[dot_index+1:]}')