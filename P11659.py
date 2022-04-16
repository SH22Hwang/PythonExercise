# print(sum(numbers[s-1:e]))
# 시간초과... 슬라이싱은 느림
# 누적합을 이용하자!

import sys


def P11659():
    N, M = map(int, input().split())
    numbers = [0] + list(map(int, input().split()))
    # 누적합 계산
    for i in range(1, N+1):
        numbers[i] += numbers[i-1]

    for _ in range(M):
        s, e = map(int, input().split())
        print(numbers[e] - numbers[s-1])


if __name__ == '__main__':
    input = sys.stdin.readline
    P11659()