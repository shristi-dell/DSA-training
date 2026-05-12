cp = float(input("Enter Cost Price: "))
student = input("Are you a student (yes/no): ")
if student== "yes":
    if cp>500:
        discount = cp*0.10
    else:
        discount = cp*0.05
else:
    if cp >500:
        discount =cp*0.08
    else:
        discount=cp*0.02

final_price = cp-discount

print("Discount =",discount)
print("Final Price =", final_price)