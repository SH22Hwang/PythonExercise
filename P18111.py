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
# 포기

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

def P18111():
    n_1, m, b = map(int, input().split())
    height = list(list(map(int, input().split())) for _ in range(n_1))

    sum_height = 0
    for x in range(n_1):
        for y in range(m):
            sum_height += height[x][y]

    narashi = 0
    demand = list(list(0 for _ in range(m)) for _ in range(n_1))

    while True:  # narashi가 0부터 height의 최댓값까지 반복, narashi가 가장 작은 것 선택
        sum_demand = 0
        for i in range(n_1):
            for j in range(m):
                demand[i][j] = narashi - height[i][j]
                sum_demand += narashi - height[i][j]

        if sum_demand > b:
            narashi -= 1
        else:
            break

    time = 0
    for i in range(n_1):
        for j in range(m):
            if demand[i][j] < 0:
                time += -2 * demand[i][j]
            elif demand[i][j] > 0:
                time += demand[i][j]

    print(time, narashi)


if __name__ == '__main__':
    P18111()
