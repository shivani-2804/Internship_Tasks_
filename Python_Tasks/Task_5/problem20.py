• Problem Name: Piling Up!
• HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem


def check_piling(cubes):
    d = deque(cubes)
    
    prev_cube = float('inf')
    
    while d:
        
        if d[0] >= d[-1]:
            current_picked = d.popleft()
        else:
            current_picked = d.pop()
            
        
        if current_picked > prev_cube:
            return "No"
            
        prev_cube = current_picked
        
    return "Yes"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        side_lengths = list(map(int, input().split()))
        print(check_piling(side_lengths))
