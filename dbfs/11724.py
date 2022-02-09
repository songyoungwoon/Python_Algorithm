import sys
from queue import Queue

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    g = [[] for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]

    for i in range(m):
        v, e = map(int, sys.stdin.readline().split())
        g[v].append(e)
        g[e].append(v)

    count = 0
    for i in range(1, n+1):
        if visit[i] == True:
            continue
        visit[i] = True
        q = Queue()
        q.put(g[i])
        while q.qsize() != 0:
            node = q.get()
            for i in node:
                if visit[i] == True:
                    continue
                visit[i] = True
                q.put(g[i])
        count += 1
    print(count)