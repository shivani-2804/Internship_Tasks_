# Problem Name: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

import os
from collections import Counter

def gameOfThrones(s):
    counts = Counter(s)
    odd_counts = sum(1 for v in counts.values() if v % 2 != 0)
    return "YES" if odd_counts <= 1 else "NO"

if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
    print(result)
