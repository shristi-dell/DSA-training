import re
str = input("enter any string")
m=re.match(str, "abc@xyz_pqr*")
if m!=None:
    print ("yes matching is availabe at beg")
    print ('start index: ' ,m.start(),'.end index:' , m.end())
else:
    
    print (" matching is not  availabe at beg")