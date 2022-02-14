import sys
import copy
from collections import deque
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    min_h = sys.maxsize
    max_h = 0
    max_count = 0
    for i in range(n):
        for j in range(n):
            if l[i][j] < min_h:
                min_h = l[i][j]
            if l[i][j] > max_h:
                max_h = l[i][j]
    for r_h in range(min_h, max_h):
        temp_l = copy.deepcopy(l)
        for i in range(n):
            for j in range(n):
                if temp_l[i][j] <= r_h:
                    temp_l[i][j] = -1
        count = 0
        dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visit = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if visit[i][j] == True:
                    continue
                if temp_l[i][j] == -1:
                    continue
                visit[i][j] = True
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
                        if temp_l[dx][dy] == -1:
                            continue
                        visit[dx][dy] = True
                        q.append((dx, dy))
                count += 1
        if max_count < count:
            max_count = count
    if max_count == 0:
        print(1)
    else:
        print(max_count)

