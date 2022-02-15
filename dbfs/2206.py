import sys
import copy
from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for i in range(n):
        line = list(input())
        for j in range(len(line) - 1):
            if int(line[j]) == 1:
                board[i][j] = -1
    no_crash = copy.deepcopy(board)
    wall_crash = copy.deepcopy(board)
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, y_n = q.popleft()
        if x == n-1 and y == m-1:
            if y_n == 0:
                print(no_crash[x][y] + 1)
            else:
                print(wall_crash[x][y] + 1)
            exit()
        for d in dxdy:
            dx, dy = x + d[0], y + d[1]
            if dx >= n or dx < 0 or dy >= m or dy < 0:
                continue
            if board[dx][dy] == 0:
                if y_n == 0 and no_crash[dx][dy] == 0:
                    no_crash[dx][dy] = no_crash[x][y] + 1
                    q.append((dx, dy, y_n))
                elif y_n == 1 and wall_crash[dx][dy] == 0:
                    wall_crash[dx][dy] = wall_crash[x][y] + 1
                    q.append((dx, dy, y_n))
            elif board[dx][dy] == -1:
                if y_n == 0:
                    wall_crash[dx][dy] = no_crash[x][y] + 1
                    q.append((dx, dy, 1))
    print(-1)
