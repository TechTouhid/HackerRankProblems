# https://www.hackerrank.com/challenges/nested-list/problem
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0
#
# Berry
# Harry


if __name__ == '__main__':
    index = 0
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([])
        students[index] = [name, score]
        index += 1

    from operator import itemgetter
    # min of all elements
    mn = min(students, key=itemgetter(1))[1]
    # remove elements equal to min
    filtered = [x for x in students if x[1] != mn]
    # get min of remaining
    mn_fil = min(filtered, key=itemgetter(1))[1]
    # filter remaining
    out = [x for x in filtered if x[1] == mn_fil]
    # getting the name
    name = [x[0] for x in out]

    for i in sorted(name):
        print(i)