if __name__ == "__main__":
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    dp = [0] * (n+1)
    if n == 1:
        print(stairs[0])
        exit()
    dp[1] = stairs[0]
    dp[2] = stairs[0] + stairs[1]
    for i in range(3, n+1):
        dp[i] = stairs[i - 1] + dp[i - 2]
        dp[i] = max(dp[i], stairs[i - 1] + stairs[i - 2] + dp[i - 3])

    print(dp[n])