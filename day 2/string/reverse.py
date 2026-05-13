#program to reverse order of words.
#input:learning python is very easy from ashish sir
#output:sir ashish from easy very is python learning

s = input("enter sentence: ")
w = s.split()
for i in range(len(w)-1, -1,-1):
    print(w[i], end=" ")