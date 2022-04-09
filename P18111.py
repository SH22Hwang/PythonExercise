# 반례 1
# // 355 32
# 4 4 36
# 15 43 61 21
# 19 33 31 55
# 48 63 1 30
# 31 28 3 8

import sys
# import math

def P18111():
    N, M, B = map(int, input().split())
    h = list(list(map(int, input().split())) for _ in range(N))
    height = sum(h, [])

    # 목표 높이를 두지 않고 0부터 256까지 모두 검사
    # target_c1 = math.ceil(sum(height) / (N*M)) +1  # 목표 높이 올림
    # target_c0 = math.ceil(sum(height) / (N*M))  # 목표 높이 올림
    # target_f0 = math.floor(sum(height) / (N*M))  # 목표 높이 내림
    # target_f1 = math.floor(sum(height) / (N*M)) -1 # 목표 높이 내림

    # 목표 높이를 두지 않고 0부터 256까지 모두 검사
    # narashi_c1 = list(target_c1 - x for x in height)  # 현재 높이와 목표 높이의 차
    # narashi_c0 = list(target_c0 - x for x in height)  # 현재 높이와 목표 높이의 차
    # narashi_f0 = list(target_f0 - y for y in height)  # 양수: 블록 쌓아야 함, 음수: 블록 빼야 함
    # narashi_f1 = list(target_f1 - y for y in height)  # 양수: 블록 쌓아야 함, 음수: 블록 빼야 함

    # time_c, time_f = 0, 0
    # time = [0] * 256
    time = {x: float("inf") for x in range(257)}
    avg = int(sum(height) / (N*M))

    for target in range(max(0, avg-10), 257):
        narashi = list(target - x for x in height)

        if sum(narashi) > B:
            break
        else:
            time[target] = 0

        for i in range(N * M):
            if narashi[i] < 0:
                time[target] += -2 * narashi[i]
            else:
                time[target] += narashi[i]

        # if target > 0 and time[target] > time[target - 1]:
        #     break

    value = [k for k, v in time.items() if min(time.values()) == v]
    print(time.get(value[-1]), value[-1])
    # print(time)

    # for i in range(N*M):
    #     if narashi_c1[i] < 0:
    #         # time_c += -2 * narashi_c1[i]
    #         time[0] += -2 * narashi_c1[i]
    #     else:
    #         time[0] += narashi_c1[i]
    #         # time_c += narashi_c1[i]
    #
    #     if narashi_c0[i] < 0:
    #         time[1] += -2 * narashi_c0[i]
    #         # time_c += -2 * narashi_c0[i]
    #     else:
    #         time[1] += narashi_c0[i]
    #         # time_c += narashi_c0[i]
    #
    #     if narashi_f0[i] < 0:
    #         time[2] += -2 * narashi_f0[i]
    #         # time_f += -2 * narashi_f0[i]
    #     else:
    #         time[2] += narashi_f0[i]
    #         # time_f += narashi_f0[i]
    #
    #     if narashi_f1[i] < 0:
    #         time[3] += -2 * narashi_f1[i]
    #         # time_f += -2 * narashi_f1[i]
    #     else:
    #         time[3] += narashi_f1[i]
    #         # time_f += narashi_f1[i]

    # if sum(narashi_c1) > B:
    #     time[0] = float('inf')
    # if sum(narashi_c0) > B:
    #     time[1] = float('inf')
    # if sum(narashi_f0) > B:
    #     time[2] = float('inf')
    # if sum(narashi_f1) > B:
    #     time[3] = float('inf')
    #
    # print(min(time), end=' ')
    # if time.index(min(time)) == 0:
    #     print(target_c1)
    # elif time.index(min(time)) == 1:
    #     print(target_c0)
    # elif time.index(min(time)) == 2:
    #     print(target_f0)
    # elif time.index(min(time)) == 3:
    #     print(target_f1)

    # if time_c > time_f:
    #     print(time_f, target_f)
    # elif time_c < time_f:
    #     print(time_c, target_c)
    # else:
    #     if target_c < target_f:
    #         print(time_f, target_f)
    #     else:
    #         print(time_c, target_c)


if __name__ == '__main__':
    input = sys.stdin.readline
    P18111()

# 마인크래프트
# 땅은 이중 리스트로 한다(0,0) ~ (m,n)
# 땅의 높이의 평균을 구하여 반올림(integer): 이상적인 땅의 높이(narashi) 그 높이로 정렬한다.
# (narashi - 각각의 땅 높이[i,j]) = 필요한 흙 블럭(damand[i,j])
# demand가 가지고 있는 흙 블럭보다 많으면 narashi 1 빼고, 다시 demand 구함
# demand가 가지고 있는 흙 블럭보다 같거나 적으면 narashi를 구했다 이제 작업 시간(time)을 구하자
# (narashi - 각각의 땅 높이)가 0이면 즉 작업이 필요 없다면 (time += 0)
# (narashi - 각각의 땅 높이)가 0보다 크면 즉 블럭을 쌓아야 하면 (time += 1)
# (narashi - 각각의 땅 높이)가 0보다 작으면 즉 블럭을 없애야 하면 (time += 2)
# time, narashi 출력

# def P18111():
#     n_1, m, b = map(int, input().split())
#     height = list(list(map(int, input().split())) for _ in range(n_1))
#
#     sum_height = 0
#     for x in range(n_1):
#         for y in range(m):
#             sum_height += height[x][y]
#     narashi = round(sum_height / (n_1*m))
#
#     demand = list(list(0 for _ in range(m)) for _ in range(n_1))
#     while True:
#         sum_demand = 0
#         for i in range(n_1):
#             for j in range(m):
#                 demand[i][j] = narashi - height[i][j]
#                 sum_demand += narashi - height[i][j]
#
#         if sum_demand > b:
#             narashi -= 1
#         else:
#             break
#
#     time = 0
#     for i in range(n_1):
#         for j in range(m):
#             if demand[i][j] < 0:
#                 time += -2 * demand[i][j]
#             elif demand[i][j] > 0:
#                 time += demand[i][j]
#
#     print(time, narashi)

# def P18111():
#     n_1, m, b = map(int, input().split())
#     height = list(list(map(int, input().split())) for _ in range(n_1))
#
#     sum_height = 0
#     for x in range(n_1):
#         for y in range(m):
#             sum_height += height[x][y]
#
#     narashi = 0
#     demand = list(list(0 for _ in range(m)) for _ in range(n_1))
#
#     while True:  # narashi가 0부터 height의 최댓값까지 반복, narashi가 가장 작은 것 선택
#         sum_demand = 0
#         for i in range(n_1):
#             for j in range(m):
#                 demand[i][j] = narashi - height[i][j]
#                 sum_demand += narashi - height[i][j]
#
#         if sum_demand > b:
#             narashi -= 1
#         else:
#             break
#
#     time = 0
#     for i in range(n_1):
#         for j in range(m):
#             if demand[i][j] < 0:
#                 time += -2 * demand[i][j]
#             elif demand[i][j] > 0:
#                 time += demand[i][j]
#
#     print(time, narashi)