from cs50 import get_string
from sys import argv
import sys


cu26 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cl26 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

while len(argv) != 2 or argv[1].isalpha() == False:
    sys.exit("Usage: python vigenere.py k")

k = argv[1]
lenk = len(argv[1])
i = 0

p = get_string("plaintext:  ")
print("ciphertext: ", end="")

for c in p:
    if c.isalpha():
        if c.isupper():
            a = k[i]
            if i < lenk - 1:
                i += 1
            else:
                i = 0
            b = ord(a)
            if a.isupper():
                b -= 65
                x = (ord(c) - 65 + b) % 26
                print(cu26[x], end="")
            else:
                b -= 97
                x = (ord(c) - 65 + b) % 26
                print(cu26[x], end="")
        if c.islower():
            a = k[i]
            if i < lenk - 1:
                i += 1
            else:
                i = 0
            b = ord(a)
            if a.isupper():
                b -= 65
                x = (ord(c) - 97 + b) % 26
                print(cl26[x], end="")
            else:
                b -= 97
                x = (ord(c) - 97 + b) % 26
                print(cl26[x], end="")
    else:
        print(c, end="")
print()