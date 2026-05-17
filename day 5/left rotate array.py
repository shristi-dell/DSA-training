# Left Rotate Array

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter number of rotations: "))

n = len(arr)
k = k % n

for _ in range(k):
    first = arr[0]

    for i in range(n - 1):
        arr[i] = arr[i + 1]

    arr[n - 1] = first

print("Array after left rotation:", arr)