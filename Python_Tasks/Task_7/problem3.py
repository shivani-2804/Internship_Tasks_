# Problem Name: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problems

import os

def marsExploration(s):
    altered = 0
    sos = "SOS"
    for i in range(len(s)):
        if s[i] != sos[i % 3]:
            altered += 1
    return altered

if __name__ == '__main__':
    s = input().strip()
    result = marsExploration(s)
    print(result)
