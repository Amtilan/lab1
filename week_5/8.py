#Write a Python program to split a string at uppercase letters.
import re

s = input()

x = re.split("[A-Z]", s)

print(x)