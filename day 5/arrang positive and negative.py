# given an array containing positive and negative no both # Arrange

arr1 = [1, -2, 3, -4, 5, -7, 9, -1]

pos = []
neg = []

for i in arr1:
  if i > 0:
    pos.append(i)

  else:
    neg.append(i)

print("Positive = ", pos)
print("Negative = ", neg)