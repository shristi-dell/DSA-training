# def selectionsort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     print(arr)

# if __name__=="__main__":
#     arr=[6,23,2,4,76,56,67,3]
#     selectionsort(arr)




#DESCENDING ORDER
def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]>arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    print(arr)

if __name__=="__main__":
    arr=[6,23,2,4,76,56,67,3]
    selectionsort(arr)