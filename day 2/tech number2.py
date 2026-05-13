# Find no is tech no. or not

n =input("Enter a no: ")
num=int(n)
length= len(n)
if length % 2==0:

    half =length // 2
    left=int(n[:half])
    right=int(n[half:])
    sum=left+right
    result = (sum)**2

    print("Sum=",sum)
    if result==num:
        print(num,"is a Tech num.")
    else:
        print(num,"is not a Tech num.")
else:
    print("Invalid: Tech nums must have an even num of digits.")