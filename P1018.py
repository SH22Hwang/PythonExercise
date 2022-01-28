# 아 시바 안해

import numpy as np


def P1018():
    row, column = map(int, input().split())  # 입력 크기
    table = np.array([[value for value in list(input())] for _ in range(row)])
    chess = np.array([['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']])

    print(table[2:10, 11])
    parity = []
    for x in range(row-7):
        for y in range(column-7):
            if table[x][y] == 'W':
               table[x:x+8, y:y+8]



            parity.append(temp)

    # print(parity)


# def P1018():
#     row, column = map(int, input().split())  # 입력 크기
#     table = np.array([[-1 if value == 'B' else 1 for value in list(input())] for _ in range(row)])
#     # 체스판 입력받아서, W는 1 B는 -1로 저장
#
#     print(table[2:10, 11])
#     parity = []
#     for x in range(row-7):
#         for y in range(column-7):
#             temp = 0
#             # parity.append(table[x:x+8, y:y+8].sum())
#             for i in range(8):
#                 temp += table[x:x+8, y+i].sum()
#             for j in range(8):
#                 temp += table[x+j, y:y+8].sum()
#
#             parity.append(temp)
#
#     print(parity)


if __name__ == '__main__':
    P1018()
