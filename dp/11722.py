if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        for j in range(i):
            if a[i] < a[j]:
                dp[i] = max(dp[i], 1 + dp[j])
        if dp[i] == 0:
            dp[i] = 1

    print(max(dp))
