def linear_search(n, arr, target):
    flag = False
    for i in range(n):
        if target!= arr[i]:
            pass
        else:
            flag = True
            loc = i
        
    if flag==True:
        print("Search is successful and present at", loc)
    else:
        print("Search is unsuccessful")

if __name__ == '__main__':
    n = int(input("Enter size: "))
    arr = []
    for i in range(n):
        arr.append(int(input()))
    target = int(input("Enter no which is to be search: "))
    linear_search(n, arr, target)