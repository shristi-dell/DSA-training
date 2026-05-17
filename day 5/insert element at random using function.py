# Insert element at randon loc using function

arr = []
n = int(input("Enter size = "))
for i in range (n):
  arr.append(int(input("Enter elements = ")))

key = int(input("Enter key = "))
loc = int(input("Enter location = "))

if 0 <= loc <= len(arr):
    arr.insert(loc, key)
    print("Array after insertion:", arr)
else:
    print("Invalid location", len(arr))