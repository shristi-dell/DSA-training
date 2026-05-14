# def add(a,b):
#     res = a + b
#     return res 

# if __name__ == '__main__':
#      a = int(input("enter a: "))
#      b = int(input("enter b: "))
#      r=add(a,b)
# print("addition is",r )



def add(a,b):
    res1 = a + b
    res2 = a + b
    res3 = a + b
    return res1,res2,res3 

if __name__ == '__main__':
     a = int(input("enter a: "))
     b = int(input("enter b: "))
     r1,r2,r3=add(a,b)
print("addition is",r1 )
print("sub is ",r2)
print("mul is ",r3)