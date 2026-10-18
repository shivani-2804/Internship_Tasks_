Problem Name: Set .discard(), .remove() & .pop()
HackerRank Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    
    command_input = input().split()
    command_name = command_input[0]
    
    if command_name == "pop":
        s.pop()
    elif command_name == "remove":
        s.remove(int(command_input[1]))
    elif command_name == "discard":
        s.discard(int(command_input[1]))

print(sum(s))
