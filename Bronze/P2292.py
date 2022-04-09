def P2292():
    n = int(input())
    sum, i = 1, 0
    while True:
        sum += 6 * i
        if sum < n:
            i += 1
            continue
        else:
            break

    print(i + 1)


if __name__ == '__main__':
    P2292()
