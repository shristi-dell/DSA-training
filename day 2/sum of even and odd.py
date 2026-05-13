n = int(input("enter size: "))
even = 0
odd = 0

for i in range(n):
    x = int(input("enter number: "))  
    if x % 2 == 0:
        even = even + x
        
    else:
        odd = odd + x
    
print("sum of even =", even)
print("sum of odd =", odd)