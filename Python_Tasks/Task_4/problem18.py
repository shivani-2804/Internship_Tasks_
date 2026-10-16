# Problem Name: Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    result_list = []
    for _ in range(N):
        command = input().split()
        action = command[0]
        if action == "insert":
            result_list.insert(int(command[1]), int(command[2]))
        elif action == "print":
            print(result_list)
        elif action == "remove":
            result_list.remove(int(command[1]))
        elif action == "append":
            result_list.append(int(command[1]))
        elif action == "sort":
            result_list.sort()
        elif action == "pop":
            result_list.pop()
        elif action == "reverse":
            result_list.reverse()
