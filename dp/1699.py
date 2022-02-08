import math

if __name__ == "__main__":
    n = int(input())
    dp = [x for x in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, math.floor(i**0.5) + 1):
            if dp[i] > dp[i - j*j] + 1:
                dp[i] = 1 + dp[i - j*j]
    print(dp[n])

