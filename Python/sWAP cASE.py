# https://www.hackerrank.com/challenges/swap-case/problem

"""
Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


def swap_case(s):
    y = ''
    for i in s:
        if i == i.lower():
            y += i.upper()
        elif i == i.upper():
            y += i.lower()
        # also can do return s.swapcase()
    return y


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
