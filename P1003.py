import sys


def P1003():
    input = sys.stdin.readline
    lines = int(input())
    cases = list(int(input()) for _ in range(lines))
    for num in cases:
        dp = [[0, 0] for _ in range(num + 1)]
        if num == 0:
            print('1 0')
        elif num == 1:
            print('0 1')
        else:
            dp[0] = [1, 0]
            dp[1] = [0, 1]
            for i in range(2, num + 1):
                dp[i][0] = dp[i-2][0] + dp[i-1][0]
                dp[i][1] = dp[i-2][1] + dp[i-1][1]
            print(dp[num][0], dp[num][1])


if __name__ == '__main__':
    P1003()