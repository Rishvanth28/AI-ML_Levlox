ch = input("Enter a sentence :")
word = ch.split()

large = word[0]

for i in ch:
    if len(i)>len(large):
        large = i
        
print(large)
