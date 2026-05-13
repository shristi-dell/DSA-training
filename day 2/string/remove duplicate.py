# write a program to remove duplicate characters
# from the given input atring?
# input:ABCDABBCDABBBCCCDDEEEF
# output:ABCDEF

s = "ABCDABBCDABBCCCDDEEEEF"
result = ""
for ch in s:
    if ch not in result:
        result = result + ch
print("Output =", result)