def P10250():
    lines = int(input())
    cases = []
    for _ in range(lines):
        cases.append(list(map(int, input().split())))  # h, w, 객실 위치

    results = []
    for i in range(lines):
        temp = []
        for j in range(1, cases[i][1] + 1):  # w
            w = str(j).zfill(2)
            for h in range(1, cases[i][0] + 1):  # h
                temp.append(str(h) + w)

        results.append(temp)

    for j in range(lines):
        print(int(results[j][cases[j][2] - 1]))


if __name__ == '__main__':
    P10250()
