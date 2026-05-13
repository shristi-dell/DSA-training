n = int(input("enter size: "))
even = 0
odd = 0
for i in range(n):
    x = int(input("enter number: "))  
    if x % 2 == 0:
        even = even + 1
        
    else:
        odd = odd + 1
    
print("total of even =", even)
print("total of odd =", odd)