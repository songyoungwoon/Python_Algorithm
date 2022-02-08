if __name__ == "__main__":
    n = int(input())

    c = list()
    for i in range(n):
        ti, pi = map(int, input().split())
        c.append((ti, pi))
    dp = [0] * (n+1)
    for i in range(n - 1, -1, -1):
        if i + c[i][0] > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(c[i][1]+ dp[i+c[i][0]], dp[i+1])
    print(dp[0])

