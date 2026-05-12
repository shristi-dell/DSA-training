ls = [3,2,3,1,2,4]
new_ls=[]
for i in ls:
    if i not in new_ls: 
        new_ls.append(i)        
print(new_ls)