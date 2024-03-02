#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

s = input()

Pattern = '[a-z]+_[a-z]+'

x = re.findall(Pattern, s)

if x:
    print(x)
else:
    print("None")




