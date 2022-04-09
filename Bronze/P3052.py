import sys


def P3052():
    nums = list(int(input()) for _ in range(10))
    remainders = set()

    for x in nums:
        remainders.add(x % 42)

    print(len(remainders))


if __name__ == '__main__':
    input = sys.stdin.readline
    P3052()
