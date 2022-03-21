banned_words = input().split(", ")
text = input()

for word in banned_words:
    replacement = "*" * len(word)
    while word in text:
        text = text.replace(word,replacement)
print(text)