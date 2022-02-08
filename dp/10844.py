if __name__ == "__main__":
    n = int(input())

    dp = [[0]*10 for _ in range(n)]
    dp[0] = [1]*10
    dp[0][0] = 0
    for i in range(1, n):
        for j in range(10):
            x, y1, y2 = i - 1, j - 1, j + 1
            if j - 1 >= 0:
                dp[i][j] += dp[x][y1]
            if j + 1 <= 9:
                dp[i][j] += dp[x][y2]
    print(sum(dp[n-1])%1000000000)