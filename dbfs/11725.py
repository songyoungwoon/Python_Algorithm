from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = int(input())
    g = [[] for _ in range(n+1)]
    answer = [0]*(n+1)
    for i in range(n - 1):
        v, e = map(int, input().split())
        g[v].append(e)
        g[e].append(v)
    q = deque()
    q.append((1, g[1]))
    visit = [False]*(n+1)
    while q:
        index, l = q.popleft()
        if visit[index] == True:
            continue
        visit[index] = True
        for i in l:
            if visit[i] == True:
                continue
            answer[i] = index
            q.append((i, g[i]))
    for i in range(2, n + 1):
        print(answer[i])