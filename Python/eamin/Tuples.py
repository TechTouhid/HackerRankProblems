
"""Sample Input 0

2
1 2
Sample Output 0

3713081631934410656"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

