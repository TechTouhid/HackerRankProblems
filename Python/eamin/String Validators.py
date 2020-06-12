"""
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""

"""
Sample Input:
qA2

Sample Output:

True
True
True
True
True
"""

if __name__ == '__main__':
    S = input()
    print(any([char.isalnum() for char in S]))
    print(any([char.isalpha() for char in S]))
    print(any([char.isdigit() for char in S]))
    print(any([char.islower() for char in S]))
    print(any([char.isupper() for char in S]))
