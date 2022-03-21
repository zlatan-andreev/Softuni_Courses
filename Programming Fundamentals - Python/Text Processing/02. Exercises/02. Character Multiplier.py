text = input().split(" ")
total_sum = 0
word1 = text[0]
word2 = text[1]

if len(word1) <= len(word2):
    max_indices = len(word1)
else:
    max_indices = len(word2)

for i in range(max_indices):
    total_sum += (ord(word1[i])*ord(word2[i]))

if len(word1) < len(word2):
    for i in word2[max_indices:]:
        total_sum+= ord(i)
elif len(word2) > len(word1):
    for i in word1[max_indices:]:
        total_sum+= ord(i)
print(total_sum)