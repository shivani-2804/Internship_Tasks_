# Problem Name: Symmetric Difference
# HackerRank Link: https://hackerrank.com

if __name__ == '__main__':
    m = int(input())
    set_a = set(map(int, input().split()))
    n = int(input())
    set_b = set(map(int, input().split()))
    sym_diff = sorted(set_a.symmetric_difference(set_b))
    for item in sym_diff:
        print(item)
