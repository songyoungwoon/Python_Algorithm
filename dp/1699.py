import math

if __name__ == "__main__":
    n = int(input())

    dp_n = math.floor(n**0.5)
    dp = [x for x in range(n + 1)]

    for i in range(2, dp_n + 1):
        for j in range(n+1):
            if i*i <= j:
                dp[j] = min(dp[j], 1 + dp[j - i*i])

    print(dp[n])