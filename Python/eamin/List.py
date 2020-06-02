"""
Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1] """

if __name__ == '__main__':
    lst = []
    N = int(input())
    for i in range(N):
        function = input().split()
        cmd = function[0]
        # print(cmd)
        arg = function[1:]
        # print(arg)
        if cmd != "print":
            cmd += "(" + ",".join(arg) + ")"
            eval("lst." + cmd)
        else:
            print(lst)
