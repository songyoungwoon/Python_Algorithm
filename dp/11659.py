input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    dp = [0] * n
    dp[0] = num[0]
    for i in range(1, n):
        dp[i] = num[i] + dp[i-1]
    for _ in range(m):
        i, j = map(int, input().split())
        if i >= 2:
            print(dp[j - 1] - dp[i - 2])
        else:
            print(dp[j - 1])

