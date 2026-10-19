# Problem Name: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english_set = set(map(int, input().split()))
    m = int(input())
    french_set = set(map(int, input().split()))
    print(len(english_set ^ french_set))
