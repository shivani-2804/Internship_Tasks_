# Problem Name: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem

import os

def funnyString(s):
    r = s[::-1]
    diff_s = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]
    diff_r = [abs(ord(r[i]) - ord(r[i+1])) for i in range(len(r)-1)]
    return "Funny" if diff_s == diff_r else "Not Funny"

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input().strip()
        result = funnyString(s)
        print(result)
