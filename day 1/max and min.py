# def find_max_min(arr):
#     maximum = arr[0]
#     minimum = arr[0]
#     for i in arr:
#         if i>maximum:
#             maximum = i
#         if i<minimum:
#             minimum = i
#     print("Maximum:",maximum)
#     print("Minimum:",minimum)
# arr = [5,3,9,2,8]
# find_max_min(arr)

arr=[5,3,9,2,8]
max=arr[0]
min=arr[0]
for i in range(1,len(arr)):
    if max<arr[i]:
        max=arr[i]
    if min>arr[i]:
        min=arr[i]

print(max)
print(min)