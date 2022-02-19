def P9095():
    lines = int(input())
    cases = list(int(input()) for _ in range(lines))
    for c in cases:
        dp = [0, 1, 2, 4] + [0 for _ in range(c)]
        for i in range(4, c+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        print(dp[c])


if __name__ == '__main__':
    P9095()
