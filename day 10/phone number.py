import re
number = input("enter any number")
m=re.fullmatch("[6-9]\\d{9}", number)
if m!=None:
    print ( number, "Valid")
   
else:
    
    print ( number, " Invalid")