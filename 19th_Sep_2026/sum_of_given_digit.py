num = int(input("Enter a number: "))

result = 0
for i in range(num):
    digit = num % 10
    result= result + digit
    num = num // 10
print("Sum of digits:", result)