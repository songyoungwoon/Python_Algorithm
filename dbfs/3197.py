from collections import deque
input = __import__('sys').stdin.readline
day = 1
s_x, s_y = 0, 0
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [['0']*c for _ in range(r)]
    water_q = deque()
    for i in range(r):
        l = list(input())
        for j in range(c):
            if l[j] == 'L':
                board[i][j] = l[j]
                s_x, s_y = i, j
            elif l[j] == 'X':
                board[i][j] = l[j]
                continue
            water_q.append((i, j))

    while water_q:
        z = len(water_q)
        for _ in range(z):
            x, y = water_q.popleft()
            count = 0
            for d in dxdy:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx < r and 0 <= dy < c:
                    if board[dx][dy] == 'X':
                        board[dx][dy] = day
                        water_q.append((dx, dy))
        day += 1
    left = 0
    right = day
    mid = (left + right) // 2
    swan_q = deque()
    while left <= right:
        meet = False
        swan_q.append((s_x, s_y))
        visit = [[False] * c for _ in range(r)]
        while swan_q:
            x, y = swan_q.popleft()
            if visit[x][y] == True:
                continue
            visit[x][y] = True
            for d in dxdy:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx < r and 0 <= dy < c:
                    if visit[dx][dy] == False and board[dx][dy] == 'L':
                        meet = True
                        swan_q.clear()
                        break
                    elif visit[dx][dy] == False and int(board[dx][dy]) <= mid:
                        swan_q.append((dx, dy))
        if meet == True:
            right = mid - 1
            mid = (left + right) // 2
        else:
            left = mid + 1
            mid = (left + right) // 2

    print(right + 1)


