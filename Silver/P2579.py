import sys


def P2579():
    m = int(input())
    step = [0] + list(int(input()) for _ in range(m)) + [0]
    dp = [0]*(m+2)

    dp[1] = step[1]
    dp[2] = step[1] + step[2]
    for x in range(3, m+1):
        dp[x] = max(dp[x-2], dp[x-3] + step[x-1]) + step[x]

    print(dp[m])


if __name__ == '__main__':
    input = sys.stdin.readline
    P2579()
