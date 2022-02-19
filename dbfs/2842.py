input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = int(input())
    s_x, s_y = 0, 0
    board = [['.']*n for _ in range(n)]
    for i in range(n):
        l = list(input())
        for j in range(n):
            board[i][j] = l[j]
            if l[j] == 'P':
                s_x, s_y = i, j
