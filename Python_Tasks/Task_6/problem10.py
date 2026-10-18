Problem Name: Designer Door Mat
HackerRank Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())
for i in range(1, N, 2):
    pattern = ('.|.' * i)
    print(pattern.center(M, '-'))

print('WELCOME'.center(M, '-'))


for i in range(N-2, 0, -2):
    pattern = ('.|.' * i)
    print(pattern.center(M, '-'))
