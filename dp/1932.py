import sys

if __name__ == "__main__":
    n = int(input())
    t = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = [[0]*i for i in range(1, n + 1)]
    dp[0][0] = t[0][0]
    for i in range(0, n - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i+1][j], dp[i][j] + t[i+1][j])
            dp[i + 1][j + 1] = max(dp[i+1][j+1], dp[i][j] + t[i+1][j+1])
    print(max(dp[n - 1]))