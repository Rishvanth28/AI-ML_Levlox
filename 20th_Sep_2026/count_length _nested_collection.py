arr = [1, 2, [3, 4, 5], 6]
count = 0

# for i in arr:
#     if type(i) != list:
#         count += 1
#     elif type(i) == list:
#         for j in range (1,len(arr)):
#             count += 1
# print(count)


for i in arr:
    if type(i) == list:
        for j in i:
            count += 1
    else:
        pass
print(count)
