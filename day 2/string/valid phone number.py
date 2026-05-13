# Accept a mobile number and check whether the mobile number is valid or not.
# A valid Indian mobile number must:

# Contain exactly 10 digits
# Start with 6, 7, 8, or 9

n = input("enter mobile number: ")
if len(n) == 10 and n[0] in "6789":
    print("Valid Indian Mobile Number")
else:
    print("Invalid Mobile Number")