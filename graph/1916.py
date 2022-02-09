import sys
from heapq import heappush, heappop

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    g = [list() for _ in range(n+1)]
    d = [sys.maxsize] * (n + 1)
    visit = [False] * (n+1)
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        g[a].append((b,c))


    src, dst = map(int, sys.stdin.readline().split())

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

    print(d[dst])

