# for i in range(1,6):
#     if i ==3:
#         continue  

#     for j in range(10,5,-1):
#         if j ==8:
#             continue
#         if i +j == 11:
#             print(i,j)


i = 1
j = 10
while i < j:
    if i == 3 and j == 8:

        i = i + 1
        j = j - 1
        continue
    print(i, "\t", j)
    i = i + 1
    j = j - 1