# Problem Name: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import os
from collections import Counter

def isValid(s):
    counts = Counter(s)
    freq_counts = Counter(counts.values())
    
    if len(freq_counts) == 1:
        return "YES"
    
    if len(freq_counts) == 2:
        (f1, c1), (f2, c2) = freq_counts.items()
        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"
        if (f1 - f2 == 1 and c1 == 1) or (f2 - f1 == 1 and c2 == 1):
            return "YES"
            
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    result = isValid(s)
    print(result)
