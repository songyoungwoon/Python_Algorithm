from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    day = 0
    while True:
        visit = [[False] * n for _ in range(n)]
        breakTrue = 0
        for i in range(n):
            for j in range(n):
                if visit[i][j] == True:
                    continue
                visit[i][j] = True
                q = deque()
                q.append((i, j))
                union = list()
                union.append((i, j))
                sum = board[i][j]
                while q:
                    x, y = q.popleft()
                    for d in dxdy:
                        dx, dy = x + d[0], y + d[1]
                        if 0<=dx<n and 0<=dy<n and not visit[dx][dy]:
                            if L<=abs(board[x][y] - board[dx][dy])<=R:
                                visit[dx][dy] = True
                                sum += board[dx][dy]
                                q.append((dx, dy))
                                union.append((dx, dy))
                if len(union) == 1:
                    breakTrue += 1
                    continue
                sum //= len(union)
                for u in union:
                    board[u[0]][u[1]] = sum
        if breakTrue == n*n:
            break
        day += 1
    print(day)