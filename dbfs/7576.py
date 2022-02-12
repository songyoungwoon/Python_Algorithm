from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    m, n = map(int, input().split())

    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))

    q = deque()
    for i in range(n):
        for j in range(m):
            if t[i][j] == 1:
                q.append((i, j))
    dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while q:
        x, y = q.popleft()
        for i in dxdy:
            dx, dy = x + i[0], y + i[1]
            if dx >= n or dx < 0 or dy >= m or dy < 0:
                continue
            if t[dx][dy] == 0:
                t[dx][dy] = t[x][y] + 1
                q.append((dx, dy))
    max_d = 0
    for i in range(n):
        for j in range(m):
            if t[i][j] == 0:
                print(-1)
                exit()
        max_d = max(max_d, max(t[i]))
    print(max_d - 1)