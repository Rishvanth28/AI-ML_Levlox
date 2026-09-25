def largest_two_numbers():
    
    num1 = int(input("Enter a num1"))
    num2 = int(input("Enter a num2"))

    if num1>num2:
        return("Num1 is Largest")
    else:
        return("Num2 is Largest")

result = largest_two_numbers()
print(result)
        
