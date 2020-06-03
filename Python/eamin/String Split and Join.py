"""Sample Input

this is a string
Sample Output

this-is-a-string"""


def split_and_join(line):
    s = line.split(' ')
    j = "-".join(s)
    return j


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


