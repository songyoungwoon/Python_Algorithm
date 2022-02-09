import sys

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    adj = [[sys.maxsize]*(n) for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        if adj[a][b] == 0:
            adj[a][b] = c
        else: adj[a][b] = min(adj[a][b], c)

    for i in range(n):
        for j in range(n):
            if i == j:
                adj[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    for i in range(n):
        for j in range(n):
            if adj[i][j] == sys.maxsize:
                adj[i][j] = 0

    for i in adj:
        print(*i)