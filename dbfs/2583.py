from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    m, n, k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(n):
            for j in range(m):
                if x1 <= i < x2 and y1 <= j < y2:
                    board[i][j] = -1
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    area_count = 0
    width_list = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                continue
            q = deque()
            q.append((i, j))
            width_count = 0
            while q:
                x, y = q.popleft()
                width_count += 1
                for d in dxdy:
                    dx, dy = x + d[0], y + d[1]
                    if dx >= n or dx < 0 or dy >= m or dy < 0:
                        continue
                    if board[dx][dy] != 0:
                        continue
                    board[dx][dy] = 1
                    q.append((dx, dy))
            if width_count == 1:
                width_list.append(width_count)
            else:
                width_list.append(width_count - 1)
            area_count += 1
    width_list.sort()
    print(area_count)
    print(*width_list)
