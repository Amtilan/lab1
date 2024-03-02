#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re 

str = input()

Pattern = '^a(b*)$'

x = re.findall(Pattern, str)

print(x)