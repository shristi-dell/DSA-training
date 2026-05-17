# Intersection of two arrays

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

arr3 = []

for i in arr1:
    if i in arr2 and i not in arr3:
        arr3.append(i)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Intersection Array:", arr3)