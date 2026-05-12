for i in range(1,10001):
    no=i
    save=no
    sum=0
    
    #count logic
    count=0
    temp=no
    while temp>0:
        count+=1
        temp//=10

    #armstrong logic
    while no>0:
        rem=no%10
        sum=sum+(rem**count)
        no//=10

    if sum==save:
        print(save)