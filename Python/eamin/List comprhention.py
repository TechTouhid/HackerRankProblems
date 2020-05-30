# # python
# x = int(input()) # 2
# y = int(input()) # 2
# n = int(input()) # 2
# ar = []
# p = 0
# # for i in range(x + 1):
# #     for j in range(y + 1):
# #         if i + j != n:
# #             ar.append([])
# #             ar[p] = [i, j]
# #             p += 1
#
#
# ea = [[i, j] for j in range(x + 1)for i in range(y + 1) if j + i != n]
#
#
# print(ea)
#

if __name__ == '__main__':

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if j + i + k != n])


