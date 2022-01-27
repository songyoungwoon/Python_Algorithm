def fibo(n):
    if n == 0:
        dp0[n] = 1
        return 0
    elif n == 1:
        dp1[n] = 1
        return 1
    else:
        if dp[n] != -1:
            return dp[n]
        else:
            dp[n] = fibo(n-1) + fibo(n-2)
            dp0[n] = dp0[n-1] + dp0[n-2]
            dp1[n] = dp1[n-1] + dp1[n-2]
            return dp[n]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        dp, dp0, dp1 = [-1]*(n+1), [0]*(n+1), [0]*(n+1)
        if n == 0:
            dp[0] = 0
        else:
            dp[0], dp[1] = 0, 1
        fibo(n)
        print(dp0[n], dp1[n])

