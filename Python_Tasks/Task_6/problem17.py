Problem Name: Check Strict Superset
HackerRank Link:https://www.hackerrank.com/challenges/py-check-strict-superset/problem



set_a = set(input().split())
is_strict_superset = True

for _ in range(int(input())):
    other_set = set(input().split())
    if not (set_a.issuperset(other_set) and len(set_a) > len(other_set)):
        is_strict_superset = False
        break

print(is_strict_superset)
