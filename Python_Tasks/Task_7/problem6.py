# Problem Name: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

import os

def pangrams(s):
    s = s.lower()
    letters = set(c for c in s if c.isalpha())
    return "pangram" if len(letters) == 26 else "not pangram"

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
