def f(n, m, c):
    z_list[n][m] = c
    z_list[n+1][m] = c+1
    z_list[n][m+1] = c+2
    z_list[n+1][m+1] = c+3

    # n+1이 아니라
    # n+2^c, c=0, 1, 2...


def P1074():
    for i in range(4**num, 4):
        f(i, i, i)
        f(i+2, i, i)
        f(i, i+2, i)
        f(i+2, i+2, i)

    print(z_list)


if __name__ == '__main__':
    num = int(input())
    z_list = [[0] * (2**num)] * 2**num
    print(z_list)
    P1074()
