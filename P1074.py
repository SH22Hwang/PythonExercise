# def f(n, m, c):
#     z_list[n][m] = c
#     z_list[n+1][m] = c+1
#     z_list[n][m+1] = c+2
#     z_list[n+1][m+1] = c+3
#
#     # n+1이 아니라
#     # n+2^c, c=0, 1, 2...
#
#
# def P1074():
#     for i in range(4**num, 4):
#         f(i, i, i)
#         f(i+2, i, i)
#         f(i, i+2, i)
#         f(i+2, i+2, i)
#
#     print(z_list)
import sys


def Divide_and_conquer(a, b, size):
    if size == 0:
        return 0

    return 2 * (a % 2) + (b % 2) + 4 * Divide_and_conquer(size - 1, int(a / 2), int(b / 2))


def P1074():
    # z[0][0] = 0
    # z[0][1] = 1
    # z[1][0] = 2
    # z[1][1] = 3

    # a, b = 0, 0
    # for x in range(0, num):
    #
    #     z[a][b+2**x] = z[a][b] + 4**x
    #
    #     z[a+2**x][b] = z[a][b+2**x] + 4**x
    #
    #     z[a+2**x][b++2**x] = z[a+2**x][b] + 4**x


    Divide_and_conquer(0, 0, num-1)
    print(Divide_and_conquer(r, c, num))


if __name__ == '__main__':
    input = sys.stdin.readline
    num, r, c = map(int, input().strip().split())
    temp = 2**num
    z = [[0]*temp] * temp
    cnt = 0
    P1074()
    print(z)
