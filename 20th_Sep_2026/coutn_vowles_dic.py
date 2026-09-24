words = ["apple", "banana", "cat"]

result = {}
vowles = "aeiou"
for word in words:
    count = 0

    for ch in word:
        if ch in vowles:
            count += 1
    result[word] = count
print(result)
