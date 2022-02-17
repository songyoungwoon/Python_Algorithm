from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = int(input())
    src, dst = map(int, input().split())
    m = int(input())

    g = [[] for _ in range(n+1)]
    visit = [False]*(n+1)
    for i in range(m):
        v, e = map(int, input().split())
        g[v].append(e)
        g[e].append(v)
    q = deque()
    q.append((g[src], 1))
    visit[src] = True
    while q:
        node, r = q.popleft()
        for i in node:
            if visit[i] == True:
                continue
            if i == dst:
                print(r)
                exit()
            else:
                visit[i] = True
                q.append((g[i], r + 1))
    print(-1)