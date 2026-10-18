Problem Name: Check Subset
HackerRank Link:https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(input())):
    _ = input()
    set_a = set(input().split())
    _ = input()
    set_b = set(input().split())
    print(set_a.issubset(set_b))
