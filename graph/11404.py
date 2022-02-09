import sys

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    adj = [[sys.maxsize]*(n+1) for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if adj[a][b] == 0:
            adj[a][b] = c
        else: adj[a][b] = min(adj[a][b], c)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                adj[i][j] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    for i in range(1, len(adj)):
        print(*adj[i][1:])