import sys


def P11399():
    length = int(input())
    numbers = sorted(list(map(int, input().split())))
    result = 0
    for i in range(length, 0, -1):
        result += numbers[-i] * i

    print(result)


if __name__ == '__main__':
    input = sys.stdin.readline
    P11399()