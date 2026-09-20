ch=input("Enter a string: ")
rev =[]
for i in range(len(ch)-1,-1,-1):
    rev.append(ch[i])
    
rev = ''.join(rev) # convert list to string([['m'], ['a'], ['d'], ['a'], ['m']] -> 'madam')
if rev == ch:
    print("Palindrom")
else:
    print("Not a Palindrom")



    