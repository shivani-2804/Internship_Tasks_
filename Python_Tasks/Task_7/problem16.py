# Problem Name: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import os

def caesarCipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr(start + (ord(char) - start + k) % 26))
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
