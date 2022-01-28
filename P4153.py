def P4153():
    pita = []
    while True:
        numbers = list(map(int, input().split()))
        numbers = sorted(numbers)
        if sum(numbers) != 0:
            pita.append(numbers)
        else:
            break

    for i in range(len(pita)):
        if pita[i][2] ** 2 == pita[i][0] ** 2 + pita[i][1] ** 2:
            print("right")
        else:
            print("wrong")


if __name__ == '__main__':
    P4153()
