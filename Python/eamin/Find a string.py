"""Sample Input:

ABCDCDC
CDC

Sample Output:

2
"""


# def count_substring(string, sub_string):
#     count = string.find(sub_string)
#     return count
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)







def count_substring(string, substring):
    c = 0
    i = -1
    while True:

        i = string.find(substring, i + 1)
        print(i)
        if i == -1:
            break
        c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
