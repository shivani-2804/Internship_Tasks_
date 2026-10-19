# Problem Name: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem

import os
from collections import Counter

def anagram(s):
    n = len(s)
    if n % 2 != 0:
        return -1
    s1, s2 = s[:n//2], s[n//2:]
    c1, c2 = Counter(s1), Counter(s2)
    return sum((c1 - c2).values())

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        print(result)
