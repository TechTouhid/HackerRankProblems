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
from operator import itemgetter

if __name__ == '__main__':
    index = 0
    list_s = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        list_s.append([])
        list_s[index] = [name, score]
        index += 1

    mn = min(list_s, key=itemgetter(1))[1]
    filtered = [x for x in list_s if x[1] != mn]
    mn_fil = min(filtered, key=itemgetter(1))[1]
    out = [i for i in filtered if i[1] == mn_fil]
    name = [i[0] for i in out]

    for i in sorted(name):
        print(i)