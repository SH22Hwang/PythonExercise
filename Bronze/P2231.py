def P2231():
    num = int(input())

    minor = num - 9 * len(str(num))
    if minor < 0: minor = 0

    temp = 0
    for i in range(minor, num):
        temp = i

        for j in str(i):
            temp += int(j)

        if num == temp:
            print(i)
            exit(0)

    if num != temp:
        print(0)


if __name__ == '__main__':
    P2231()