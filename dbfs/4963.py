from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == 0 or h == 0:
            exit()
        m = [list(map(int, input().split())) for _ in range(h)]
        visit = [[False]*w for _ in range(h)]
        count = 0
        for i in range(h):
            for j in range(w):
                if m[i][j] == 0:
                    continue
                if visit[i][j] == True:
                    continue
                q = deque()
                q.append((i, j))
                dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                while q:
                    x, y = q.popleft()
                    for d in dxdy:
                        dx, dy = x + d[0], y + d[1]
                        if dx >= h or dx < 0 or dy >= w or dy < 0:
                            continue
                        if m[dx][dy] == 0:
                            continue
                        if visit[dx][dy] == True:
                            continue
                        visit[dx][dy] = True
                        q.append((dx, dy))
                count += 1
        print(count)

