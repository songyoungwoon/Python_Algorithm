from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = int(input())
    board = [[0]*n for _ in range(n)]

    q = deque()
    for i in range(n):
        l = list(map(int, input().split()))
        for j in range(n):
            board[i][j] = l[j]
            if l[j] == 9:
                q.append((i, j))

