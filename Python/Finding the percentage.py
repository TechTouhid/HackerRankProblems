# https://www.hackerrank.com/challenges/finding-the-percentage/problem

"""
Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 1
26.50
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sumOfMarks = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in student_marks[query_name]:
        sumOfMarks += i

    print(f"{sumOfMarks / len(student_marks[query_name]):.2f}")
