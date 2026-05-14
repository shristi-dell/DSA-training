def binary_search(n,arr,target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            flag=True
            loc=mid
        
        elif arr[mid]>target:
            high=mid-1
        elif target>arr[mid]:
            low=mid+1
    if flag==True:
        print("Search is successful and present at:", loc)
    else:
        print("Search is unsuccessful")
            
        
if __name__ == "__main__":
    n=int(input("Enter size: "))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    target=int(input("Enter no which is to be search: "))
    binary_search(n, arr, target)