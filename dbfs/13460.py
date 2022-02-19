from collections import deque
input = __import__('sys').stdin.readline
def moveToEnd(x, y, ox, oy, d):
    hole, back = False, False
    tx, ty = x, y
    while True:
        dx, dy = tx + d[0], ty + d[1]
        if board[dx][dy] == '#':
            break
        tx, ty = dx, dy
        if board[dx][dy] == 'O':
            hole = True
            break
        if (dx, dy) == (ox, oy):
            back = True
    if back == True:
        tx, ty = tx - d[0], ty - d[1]

    return tx, ty, hole

if __name__ == "__main__":
    n, m = map(int, input().split())
    r_x, r_y, b_x, b_y = 0, 0, 0, 0
    board = [['#']*m for _ in range(n)]
    for i in range(n):
        l = list(input())
        for j in range(m):
            if l[j] != '#':
                board[i][j] = l[j]
                if l[j] == 'R':
                    r_x, r_y = i, j
                if l[j] == 'B':
                    b_x, b_y = i, j

    q = deque()
    q.append((r_x, r_y, b_x, b_y, 0))
    dxdy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visit = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count >= 10:
            continue
        for d in dxdy:
            rhole, bhole = False, False
            rdx, rdy, rhole = moveToEnd(rx, ry, bx, by, d)
            bdx, bdy, bhole = moveToEnd(bx, by, rx, ry, d)
            if bhole == True:
                continue
            elif rhole == True:
                print(count + 1)
                exit()
            if not visit[rdx][rdy][bdx][bdy]:
                visit[rdx][rdy][bdx][bdy] = True
                q.append((rdx, rdy, bdx, bdy, count + 1))
#            if (rdx, rdy, bdx, bdy) != (rx, ry, bx, by):
#                q.append((rdx, rdy, bdx, bdy, count + 1))
    print(-1)