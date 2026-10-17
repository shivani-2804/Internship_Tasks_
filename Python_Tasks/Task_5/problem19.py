• Problem Name: Merge the Tools!
• HackerRank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        
        sub_segment = string[i:i + k]
        
        
        
        unique_chars = dict.fromkeys(sub_segment)
        
        
        print("".join(unique_chars.keys()))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)