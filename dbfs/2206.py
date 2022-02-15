import sys
import copy
from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    board[0][0] = 2
    for i in range(n):
        line = list(input())
        for j in range(len(line) - 1):
            if int(line[j]) == 1:
                board[i][j] = -1
    min_count = sys.maxsize
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, y_n = q.popleft()
        for d in dxdy:
            dx, dy = x + d[0], y + d[1]
            if dx >= n or dx < 0 or dy >= m or dy < 0:
                continue
            if board[dx][dy] == 0:
                board[dx][dy] = board[x][y] + 1
                q.append((dx, dy, y_n))
            elif board[dx][dy] != -1:
                board[dx][dy] = min(board[dx][dy], board[x][y] + 1)
            else:
                if y_n == 0:
                    board[dx][dy] = board[x][y] + 1
                    q.append((dx, dy, 1))
    print(board[n-1][m-1] - 1)