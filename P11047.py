def P11047():
    lines, money = map(int, input().split())
    coins = sorted(list(int(input()) for _ in range(lines)))

    # 시간 초과, 다른 알고리즘으로 바꾸기
    # result = 0
    # for i in range(-1, -1*lines - 1, -1):
    #     while money >= coins[i]:
    #         money -= coins[i]
    #         result += 1
    #
    # print(result)

    result = 0
    for i in range(-1, -1*lines - 1, -1):
        if money // coins[i] > 0:
            num = money // coins[i]
            money = money % coins[i]
            result += num

    print(result)


if __name__ == '__main__':
    P11047()