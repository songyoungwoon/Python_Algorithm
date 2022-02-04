if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))

    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[1][1] = p[0]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j >= i:
                dp[i][j] = max(dp[i - 1][j], p[i - 1] + dp[i][j - i])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][n])