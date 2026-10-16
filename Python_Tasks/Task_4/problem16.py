# Problem Name: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    grades = sorted(list(set([score for name, score in students])))
    second_lowest_grade = grades[1]
    result_names = sorted([name for name, score in students if score == second_lowest_grade])
    for name in result_names:
        print(name)
