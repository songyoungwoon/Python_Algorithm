from queue import Queue

def dfs(n):
    global g
    global s
    global dfs_str

    for i in g[n]:
        if s.__contains__(i):
            continue
        dfs_str += " " + str(i)
        s.add(i)
        dfs(i)

if __name__ == "__main__":
    n, m, v = map(int, input().split())

    g = [list() for _ in range(n + 1)]
    for i in range(m):
        V, E = map(int, input().split())
        g[V].append(E)
        g[E].append(V)
    for i in range(1, n + 1):
        g[i].sort()

    dfs_str = str(v)
    bfs_str = str(v)

    s = set()
    s.add(v)
    dfs(v)

    s.clear()
    q = Queue()
    q.put(g[v])
    s.add(v)
    while q.qsize() != 0:
        node = q.get()
        for i in node:
            if s.__contains__(i):
                continue
            s.add(i)
            bfs_str += " " + str(i)
            q.put(g[i])

    print(dfs_str)
    print(bfs_str)