# https://www.hackerrank.com/challenges/finding-the-percentage/problem
#


"""
Sample Output 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 1

26.50 """

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # print(student_marks)
    query_name = input()
    n = student_marks[query_name]
    s = 0
    for i in n:
        s += i
    index = len(n)
    last = (s / index)
    print(f'{last:.2f}')
