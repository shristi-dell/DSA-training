arr=[[1,2,3],22,[4,5]]
print(arr)
for x in range(len(arr)):
    print(arr[x])


arr=[[1,2,3],[4,5],[7,8,9]]
print(arr)
for x in range(len(arr)):
    print(arr[x])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()