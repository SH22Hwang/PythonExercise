import sys


def P8958():
    num = int(input())
    cases = list(input() for _ in range(num))

    for c in cases:
        cnt, result = 0, 0
        for x in c:
            if x == 'O':
                cnt += 1
                result += cnt
            else:
                cnt = 0
        print(result)


if __name__ == '__main__':
    input = sys.stdin.readline
    P8958()
