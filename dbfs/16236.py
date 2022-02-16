import sys
from collections import deque
input = __import__('sys').stdin.readline
size = 2
finish_time = 0
board_sum = 0
eat_count = 0
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    q = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                q.append((i, j, 0))
    while q:
        near = []
        move_count = sys.maxsize
        visit = [[False] * n for _ in range(n)]
        while q:
            x, y, c = q.popleft()
            if visit[x][y] == True:
                continue
            if c == move_count:
                continue
            visit[x][y] = True
            for d in dxdy:
                dx, dy = x + d[0], y + d[1]
                if dx >= n or dx < 0 or dy >= n or dy < 0:
                    continue
                if board[dx][dy] != 0 and board[dx][dy] < size:
                    near.append((dx, dy))
                    move_count = c + 1
                    continue
                if board[dx][dy] == 0 or board[dx][dy] <= size:
                    q.append((dx, dy, c + 1))
        if move_count != sys.maxsize:
            finish_time += move_count
        if len(near) != 0:
            near.sort(key=lambda x:(x[0], x[1]))
            nx, ny = near.pop(0)
            board[nx][ny] = 0
            q.append((nx, ny, 0))
            eat_count += 1
        if eat_count == size:
            eat_count = 0
            size += 1
    print(finish_time)