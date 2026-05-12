number = int(input("enter number: "))
n1 = number % 10 # 3
no = number // 10 # 12
n2 = no % 10 # 2
no = no // 10 # 1
n3 = no % 10 # 1
rev = n1 * 100 + n2 * 10 + n3
print(rev)