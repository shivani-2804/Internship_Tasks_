# Problem Name: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    num_customers = int(input())
    inventory = Counter(shoe_sizes)
    total_revenue = 0
    for _ in range(num_customers):
        size, price = map(int, input().split())
        if inventory[size] > 0:
            total_revenue += price
            inventory[size] -= 1
    print(total_revenue)
