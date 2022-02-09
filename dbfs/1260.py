from queue import Queue

def dfs(n):
    global dfs_str

    for i in g[n]:
        if visit[i] == True:
            continue
        visit[i] = True
        dfs_str += " " + str(i)
        dfs(i)

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    dfs_str = str(v)
    bfs_str = str(v)

    g = [list() for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    visit[v] = True
    for i in range(m):
        V, E = map(int, input().split())
        g[V].append(E)
        g[E].append(V)
    for i in range(1, n + 1):
        g[i].sort()
    dfs(v)

    visit = [False for _ in range(n + 1)]
    visit[v] = True
    q = Queue()
    q.put(g[v])
    while q.qsize() != 0:
        node = q.get()
        for i in node:
            if visit[i] == True:
                continue
            visit[i] = True
            bfs_str += " " + str(i)
            q.put(g[i])

    print(dfs_str)
    print(bfs_str)