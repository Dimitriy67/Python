# Напишите программу, которая определяет, является ли скобочная последовательность правильной.
from re import search, sub

s = input()
pattern = r'\(\)'

while search(pattern, s):
    s = sub(pattern, '', s)

print(bool(not s))