Problem Name: Set .union() Operation
HackerRank Link:https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english_subs = set(map(int, input().split()))
m = int(input())

french_subs = set(map(int, input().split()))


at_least_one_sub = english_subs.union(french_subs)

print(len(at_least_one_sub))
