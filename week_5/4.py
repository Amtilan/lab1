#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

s = input()

Pattern = '[A-Z]{1}[a-z]+'

x = re.findall(Pattern, s)

if x:
    print(x)
else:
    print("None")