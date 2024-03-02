#Write a python program to convert snake case string to camel case string.
import re

#snake_case - the style of writing in which each space is replaced by an underscore (_) character, 
#and the first letter of each word written in lowercase.

#camelCase - стиль написания составных слов, 
#при котором несколько слов пишутся слитно без пробелов, при этом каждое слово внутри фразы пишется с прописной буквы.

s = input()

def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel(s))