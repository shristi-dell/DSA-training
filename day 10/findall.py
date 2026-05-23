#findall(): to find all occurrences of the matches

import re
list=re.findall("[0-9]","ab4#hf7p@5qr9")
print(list)
for x in list:
    print(x)
