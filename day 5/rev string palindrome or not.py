# Reverse string and check whether it is palindrome or not

s = "A man, a plan, a canal: Panama"

str = ""

for i in s:
    if i.isalpha():
        str = str + i.lower()

rev = ""

for i in range(len(str) - 1, -1, -1):
    rev = rev + str[i]

print("clean String :", str)
print("Reversed String:", rev)


if str == rev:
    print("\n Palindrome")
else:
    print("\n Not Palindrome")