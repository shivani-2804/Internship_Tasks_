Problem Name: Set Mutations
HackerRank Link: https://www.hackerrank.com/challenges/py-set-mutations/problem


_ = input()
set_a = set(map(int, input().split()))

for _ in range(int(input())):
    operation, _ = input().split()
    other_set = set(map(int, input().split()))
    getattr(set_a, operation)(other_set)

print(sum(set_a))
