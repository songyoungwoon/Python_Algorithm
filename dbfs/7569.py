from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    m, n, h = map(int, input().split())
    t = [[[0]*m for _ in range(n)] for _ in range(h)]
    ripe = deque()
    for i in range(h):
        for j in range(n):
            l = list(map(int, input().split()))
            for z in range(len(l)):
                t[i][j][z] = l[z]
                if l[z] == 1:
                    ripe.append((i,j,z))
    max = 0
    while ripe:
        z, x, y = ripe.popleft()
        dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dzdz = [1, -1]
        for i in dxdy:
            dx, dy = x + i[0], y + i[1]
            if dx >= n or dx < 0 or dy >= m or dy < 0:
                continue
            if t[z][dx][dy] == 0:
                t[z][dx][dy] = t[z][x][y] + 1
                ripe.append((z, dx, dy))
                if max < t[z][x][y] + 1:
                    max = t[z][x][y] + 1
        for i in dzdz:
            dz = z + i
            if dz >= h or dz < 0:
                continue
            if t[dz][x][y] == 0:
                t[dz][x][y] = t[z][x][y] + 1
                ripe.append((dz, x, y))
                if max < t[z][x][y] + 1:
                    max = t[z][x][y] + 1
    count = 0
    for i in range(h):
        for j in range(n):
            for z in range(m):
                if t[i][j][z] == 0:
                    print(-1)
                    exit()
    if max == 0:
        print(0)
    else:
        print(max - 1)

