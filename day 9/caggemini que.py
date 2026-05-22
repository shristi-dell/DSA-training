# Capgemini
# Problem Statement: Raj wants to know the maximum marks scored by
#  him in each semester. The mark should be between 0 to 100, 
# if it goes beyond the range display "You have entered invalid mark."

# Sample Input 1:
# Enter no of semester: 3
# Enter no of subjects in 1 semester: 3
# Enter no of subjects in 2 semester: 4
# Enter no of subjects in 3 semester: 2

# Marks obtained in semester 1:
# 50
# 60
# 70

# Marks obtained in semester 2:
# 90
# 98
# 76
# 67

# Marks obtained in semester 3:
# 89
# 76

# Sample Output 1:
# Maximum mark in 1 semester:70
# Maximum mark in 2 semester:98
# Maximum mark in 3 semester:89


n = int(input("Enter no of semester: "))
i = 1
while i <= n:
    s = int(input("Enter no of subjects in " + str(i) + " semester: "))
    marks = []
    print("Marks obtained in semester " + str(i) + ":")
    j = 1
    flag = True
    while j <= s:
        m = int(input())
        if m < 0 or m > 100:
            print("You have entered invalid mark.")
            flag = False
            break
        marks.append(m)
        j += 1
    if flag == True:
        mx = marks[0]
        for k in marks:
            if k > mx:
                mx = k
        print("Maximum mark in " + str(i) + " semester:" + str(mx))
    i += 1