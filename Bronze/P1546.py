import sys


def P1546():
    num = int(input())
    numbers = list(map(int, input().split()))
    print(sum(numbers) / max(numbers) * 100 / num)


if __name__ == '__main__':
    input = sys.stdin.readline
    P1546()
