input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    num = []
    for i in range(n):
        num.append(list(map(int, input().split())))
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = num[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
    for i in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        print(dp[x2][y2] - dp[x2][y1] - dp[x1][y2] + dp[x1][y1])
