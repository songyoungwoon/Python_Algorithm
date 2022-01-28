import sys

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (n)
    dp[0] = a[0]
    for i in range(1, n):
        dp[i] = max(a[i] + dp[i - 1], a[i])
    print(max(dp))