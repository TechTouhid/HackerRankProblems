"""
Example:

# >>> string = "abracadabra"
You can access an index by:

# >>> print string[5]
a
What if you would like to assign a value?

# >>> string[5] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

Example:

# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
abrackdabra
Another approach is to slice the string and join it back.

Example:

# >>> string = string[:5] + "k" + string[6:]
# >>> print string


abrackdabra

Sample Input:

abracadabra
5 k
Sample Output:

abrackdabra  """


def mutate_string(string, position, character):
    f1 = string[:position] + f"{character}" + string[position + 1:]
    return f1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
