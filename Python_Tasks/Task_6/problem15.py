Problem Name: Set .difference() Operation
HackerRank Link:https://www.hackerrank.com/challenges/py-set-difference-operation/problem


_ = input()
english_subs = set(input().split())
_ = input()
french_subs = set(input().split())

print(len(english_subs - french_subs))
