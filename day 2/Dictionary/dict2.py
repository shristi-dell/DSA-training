rec={}
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter name: ")
    per=float(input("Enter percentage: "))
    rec[name]=per
print(rec)
for x in rec:
    print(x,rec[x])