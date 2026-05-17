# Insert element at randon loc

arr = []
n = int(input("Enter size = "))
for i in range (n):
  arr.append(int(input("Enter elements = ")))

key = int(input("Enter key = "))
loc = int(input("Enter location = "))

arr.append(0)
# print(arr[i])

for i in range (len(arr) -1, loc, -1):
  arr[i] = arr[i-1]
arr[loc] = key
print("Array after insertion:", arr)

# if 0 <= loc <= len(arr):
#     arr.insert(loc, key)
#     print("Array after insertion:", arr)
# else:
#     print("Invalid location", len(arr))