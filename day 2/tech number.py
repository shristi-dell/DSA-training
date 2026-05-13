# A number is called a Tech Number if the given number
#  has an even number of digits and the number can be divided exactly into
#  two parts from the middle. After equally dividing the number, 
# sum up the numbers and find the square of the sum. If we get the number itself as square, 
# the given number is a Tech Number, else it is not a Tech Number.
# Example:
# 2025 is a Tech Number.

# 2025 = 20 25
# 20 + 25 = 45
# 45 * 45 = 2025


no=int(input("Enter number: "))
n1= no %100
n2= no //100
sum=n1+n2
sq=sum*sum
if sq==no:
    print("Technumber")
else:
    print("Not a Technumber")