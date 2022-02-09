import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    src = int(sys.stdin.readline())

    g = [list() for _ in range(V+1)]
    d = [sys.maxsize] * (V + 1)
    visit = [False] * (V+1)
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        g[u].append((v, w))

    d[src] = 0
    q = []
    heappush(q, (0,src))
    while q:
        value, index = heappop(q)
        if visit[index] == True:
            continue
        visit[index] = True
        for i in g[index]:
            d[i[0]] = min(d[i[0]], value + i[1])
            heappush(q, (d[i[0]], i[0]))

    for i in range(1, V + 1):
        if d[i] == sys.maxsize:
            print('INF')
        else:
            print(d[i])


