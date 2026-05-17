# Reverse the string

s = "Hello"

rev = ""

for i in range(len(s)-1, -1, -1):
    rev = rev + s[i]

print(rev)