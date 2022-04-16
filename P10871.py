import sys

def P10871():
    N, x = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in nums:
        if i < x:
            print(i, end=' ')


if __name__ == '__main__':
    input = sys.stdin.readline
    P10871()