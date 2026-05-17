# Reverse string and check palindrome using slicing

s = "A man, a plan, a canal: Panama"

str1 = ""

for i in s:
    if i.isalpha():
        str1 = str1 + i.lower()

print("Original String:", str1)

rev = str1[::-1]

print("Reversed String:", rev)

if str1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")