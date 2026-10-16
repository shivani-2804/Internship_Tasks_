# Problem Name: String Split and Join
# HackerRank Link: https://hackerrank.com

def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
