# Check if two string are anagram of eachother or not

a = "listen"
b = "silent"

if sorted(a) == sorted(b):
  print("Anagram")
else:
  print("Not Anagram")


#   An anagram means:

# Two words or strings that contain the same letters, but in a different order.

# Example:

# listen → silent

# Both words contain the same letters:

# l
# i
# s
# t
# e
# n

# So they are anagrams.

# Another example:

# evil → vile

# Anagram ✅

# Not an anagram example:

# hello → world