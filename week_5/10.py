#Write a Python program to convert a given camel case string to snake case.
import re

n = input()

def camel_to_snake(text):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake(n))