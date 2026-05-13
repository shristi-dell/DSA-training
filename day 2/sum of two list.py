# arr = []
# n = int(input("Enter size: "))
# print("Enter list elements:")
# for i in range(n):
#     ele = int(input("Enter element: "))
#     arr.append(ele)
# total = sum(arr)
# print("Sum of list:", total)



n= int(input("enter size: "))
print("enter list element: ")
arr=[]
sum=0
for i in range(n):
    ele=int(input("enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    sum=sum+arr[i]
    