import sys
if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    item = [(0,0)]
    for i in range(n):
        v,c,k = map(int, sys.stdin.readline().split())
        bit = 1
        while k > 0:
            bit_k = min(bit, k)
            item.append((v*bit_k, c*bit_k))
            k -= bit_k
            bit *= 2

    dp = [[0]*(m+1) for _ in range(len(item))]
    for i in range(1, len(item)):
        for j in range(1, m+1):
            if j >= item[i][0]:
                dp[i][j] = max(item[i][1] + dp[i - 1][j - item[i][0]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[len(item) - 1][m])