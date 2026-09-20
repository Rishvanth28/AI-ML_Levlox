arr1 = list(map(int,input("Enter array1:").split()))
arr2 = list(map(int,input("Enter array2:").split()))

# for i in arr1:
#     if i in arr2:
#         print(i,end=" ")


common = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            common.append(arr1[i])
print(common)
        
