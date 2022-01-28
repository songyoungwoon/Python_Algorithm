if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        max_count = 0
        for j in range(1, i):
            if a[i - 1] > a[i - 1 - j]:
                dp[i] = max(dp[i], dp[i - j] + 1)
            else:
                dp[i] = max(dp[i], 1)

    print(max(dp))

