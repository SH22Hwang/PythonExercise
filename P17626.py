# 알고리즘 분류
# 다이나믹 프로그래밍
# 브루트포스 알고리즘

from itertools import combinations_with_replacement
import time


# # 시간 초과
# def P17626():
#     num = int(input())
#     # if int(num ** 0.5) == num ** 0.5:
#     #     print(1)
#     #     exit(0)
#     #
#     squares = list(x ** 2 for x in range(1, int(num ** 0.5)+1))
# #     for i in range(2, 5):
# #         for case in combinations_with_replacement(squares, i):
# #             if sum(case) == num:
# #                 print(case)
# #                 print(i)
# #                 exit(0)
#
#     for x in range(1, num):
#         if int(x ** 0.5) == x ** 0.5:
#             print(x)
#             continue
#         for i in range(2, 5):
#             for case in combinations_with_replacement(squares, i):
#                 if sum(case) == x:
#                     print(x, case)
#                     break
#                     # print(i)
#                     # exit(0)

def P17626():
    num = int(input())
    dp = [4 for _ in range(num+1)]

    length = int(num ** 0.5) + 1
    squares = list(x ** 2 for x in range(1, length))

    for s in squares:
        dp[s] = 1

    for i in squares:
        for j in squares[squares.index(i):]:
            if i + j > num:
                break
            if dp[i+j] == 4:
                dp[i+j] = 2

    for x in squares:
        for y in squares[squares.index(x):]:
            for z in squares[squares.index(y):]:
                if x + y + z > num:
                    break
                if dp[x+y+z] == 4:
                    dp[x+y+z] = 3

    print(dp[num])


if __name__ == '__main__':
    P17626()
