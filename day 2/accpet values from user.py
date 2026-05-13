#accept values from user and print it
n = int(input("enter size: "))
print("enter list element: ")
arr=[]

for i in range(n):
    ele=int(input("enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    print(arr[i])

