no = 1234
sum = 0
while no>0:
    digit = no%10
    sum = sum+digit
    no = no // 10
print(sum)