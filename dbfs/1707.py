input = __import__('sys').stdin.readline
if __name__ == "__main__":
    k = int(input())
    for i in range(k):
        V, E = map(int, input().split())
        g = [[] for _ in range(V + 1)]
        group1 = set()
        group2 = set()
        for j in range(E):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
