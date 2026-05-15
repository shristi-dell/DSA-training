#ascending order

# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j + 1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     print(arr)
# if __name__ == "__main__":
#     arr = [6, 23, 2, 4, 76, 56, 67, 3]
#     bubblesort(arr)
#     # print(*arr)




#descending
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]<arr[j + 1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
if __name__ == "__main__":
    arr = [6, 23, 2, 4, 76, 56, 67, 3]
    bubblesort(arr)
    # print(*arr)