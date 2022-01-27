import sys

if __name__ == "__main__":
    n = int(input())
    price = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = [[0, 0, 0] for _ in range(n+1)]
    dp[0] = price[0]
    color = [0, 1, 2]
    for i in range(1, n):
        for j in range(3):
            min_sum = sys.maxsize
            for c in color:
                if c == j:
                    continue
                if min_sum > dp[i - 1][c]:
                    min_sum = dp[i - 1][c]
            dp[i][j] = min_sum + price[i][j]
    print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
