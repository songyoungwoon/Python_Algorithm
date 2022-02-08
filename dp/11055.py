if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = a[0]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], a[i] + dp[j])
        if dp[i] == 0:
            dp[i] = a[i]

    print(max(dp))