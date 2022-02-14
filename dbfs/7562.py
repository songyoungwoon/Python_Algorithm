from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    t = int(input())
    dxdy = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    for i in range(t):
        l = int(input())
        s_x, s_y = map(int, input().split())
        d_x, d_y = map(int, input().split())
        if s_x == d_x and s_y == d_y:
            print(0)
            continue
        board = [[0]*l for _ in range(l)]
        q = deque()
        q.append((s_x, s_y))
        while q:
            x, y = q.popleft()
            if x == d_x and y == d_y:
                print(board[d_x][d_y])
                break
            for d in dxdy:
                dx, dy = x + d[0], y + d[1]
                if dx >= l or dx < 0 or dy >= l or dy < 0:
                    continue
                if board[dx][dy] == 0 and (dx, dy) != (s_x, s_y):
                    board[dx][dy] = board[x][y] + 1
                    q.append((dx, dy))

