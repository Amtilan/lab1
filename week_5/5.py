#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

s = input()

Pattern = 'a.*?b$'

x = re.findall(Pattern, s)

if x:
    print(x)
else:
    print("None")