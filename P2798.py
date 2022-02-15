def P2798():
    num, maxint = map(int, input().split())
    cards = list(map(int, input().split()))

    cases = []
    for c1 in range(num):
        for c2 in range(c1 + 1, num):
            for c3 in range(c2 + 1, num):
                cases.append(cards[c1] + cards[c2] + cards[c3])

    cases.sort(reverse=True)
    for i in cases:
        if i <= maxint:
            print(i)
            break


if __name__ == '__main__':
    P2798()
