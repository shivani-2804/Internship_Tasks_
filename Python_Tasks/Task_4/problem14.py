# Problem Name: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input())
    country_set = set()
    for _ in range(n):
        country_set.add(input().strip())
    print(len(country_set))
