if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        dp0, dp1 = [0]*(n+1), [0]*(n+1)
        if n == 0:
            dp0[0] = 1
        else:
            dp0[0], dp1[1] = 1, 1
        for i in range(2, n+1):
            dp0[i] = dp0[i - 1] + dp0[i - 2]
            dp1[i] = dp1[i - 1] + dp1[i - 2]

        print(dp0[n], dp1[n])

