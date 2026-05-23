import re
str = input("enter any string")
m=re.fullmatch(str, "abcabcabc")
if m!=None:
    print ("yes matching is availabe at beg")

else:
    
    print (" matching is not  availabe at beg")