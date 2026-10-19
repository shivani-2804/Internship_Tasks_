# Problem Name: CamelCase
# HackerRank Link: https://www.hackerrank.com/challenges/camelcase/problem

import os

def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1

if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)
