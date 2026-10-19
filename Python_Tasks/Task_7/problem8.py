# Problem Name: Gemstones
# HackerRank Link: https://www.hackerrank.com/challenges/gem-stones/problem

import os

def gemstones(arr):
    sets = [set(s) for s in arr]
    common = set.intersection(*sets)
    return len(common)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)
