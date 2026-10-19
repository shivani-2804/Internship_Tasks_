# Problem Name: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import os

def weightedUniformStrings(s, queries):
    weights = set()
    prev_char = ""
    current_weight = 0
    
    for char in s:
        weight = ord(char) - ord('a') + 1
        if char == prev_char:
            current_weight += weight
        else:
            current_weight = weight
            prev_char = char
        weights.add(current_weight)
        
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    s = input()
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
