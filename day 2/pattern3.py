# A       B       C       D
# E       F       G       H
# I       J       K       L
# M       N       O       P

n=64
for i in range(1,5):
    for j in range(1,5):
        n=n+1
        print(chr(n),end="\t")
    print()