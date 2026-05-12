no = 145
save = no
sum = 0
while no>0:
    rem=no %10
    fact=1
    i =1

    while i <= rem:
        fact =fact * i
        i = i+1
    sum = sum+fact
    no = no//10
if sum == save:
    print("Peterson Number")
else:
    print("Not Peterson Number")