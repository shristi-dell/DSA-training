
no = int(input("Enter 9 digit number: "))
n1 = no % 10
n2 = no // 100000000
res = n1 + n2
print(res)