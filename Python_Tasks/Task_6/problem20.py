Problem Name: Validating the Phone Number
HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com


import re

for _ in range(int(input())):
    if re.match(r'^[789]\d{9}$', input().strip()):
        print("YES")
    else:
        print("NO")
