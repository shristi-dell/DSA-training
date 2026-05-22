# Capgemini in its online written test has a coding question,
#  wherein the students are given a string with multiple characters that are 
# repeated consecutively. You're supposed to reduce the size of this string using 
# mathematical logic given as in the example below:

# Input :
# aabbbbeeeeffffgggg

# Output :
# a2b4e4f4g4

# Input :
# abbcccc

# Output :
# ab2c4

def compress_string(s):
    result = ""
    i = 0
    
    while i < len(s):
        char = s[i]
        count = 1
        
        while i + count < len(s) and s[i + count] == char:
            count += 1
        
        if count > 1:
            result += char + str(count)
        else:
            result += char
        
        i += count
    
    return result

print(compress_string("aabbbbeeeeffffgggg"))
print(compress_string("abbcccc"))