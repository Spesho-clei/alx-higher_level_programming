#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if 'a' <= c <= 'z':
            print(chr(ord(c) - ord('a') + ord('A')), end="")
        else:
            print(c, end="")
    print()
