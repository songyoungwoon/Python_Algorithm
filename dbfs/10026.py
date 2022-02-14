import copy
from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = int(input())
    board = []
    rgb = [list(input()) for _ in range(n)]
    rrb = copy.deepcopy(rgb)

    for i in range(n):
        for j in range(n):
            if rgb[i][j] == 'G':
                rrb[i][j] = 'R'

    board.append(rgb)
    board.append(rrb)
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = []
    for b in board:
        count = 0
        visit = [[False]*n for _ in range(n)]
        color = ''
        for i in range(n):
            for j in range(n):
                if visit[i][j] == True:
                    continue
                visit[i][j] = True
                color = b[i][j]
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in dxdy:
                        dx, dy = x + d[0], y + d[1]
                        if dx >= n or dx < 0 or dy >= n or dy < 0:
                            continue
                        if visit[dx][dy] == True:
                            continue
                        if b[dx][dy] == color:
                            visit[dx][dy] = True
                            q.append((dx, dy))
                count += 1
        answer.append(count)
    print(answer[0], answer[1])

