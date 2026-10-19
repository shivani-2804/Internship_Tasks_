# Problem Name: String Construction
# HackerRank Link: https://www.hackerrank.com/challenges/string-construction/problem

import os

def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        print(result)
