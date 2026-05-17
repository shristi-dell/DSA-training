# Delete element from array

arr = []
n = int(input("Enter size = "))
for i in range (n):
  arr.append(int(input("Enter elements = ")))

loc = int(input("Enter location = "))

if 0 <= loc < len(arr):
    for i in range(loc, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()
    print("Array after deletion:", arr)