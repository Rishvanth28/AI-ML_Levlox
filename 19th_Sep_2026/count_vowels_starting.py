ch = input("Enter a sentence :")
word = ch.split()
count = 0
for i in word:
    first = i[0]
    if first in "aeiou":
        count += 1
print(count)
