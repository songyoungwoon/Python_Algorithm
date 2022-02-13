from itertools import combinations
from collections import deque
import copy
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    mul = [i for i in range(n*m)]
    l = [list(map(int, input().split())) for _ in range(n)]

    b = []
    for i in range(n):
        for j in range(m):
            if l[i][j] == 2:
                b.append((i, j))

    max = 0
    c = list(combinations(mul, 3))
    for i in c:
        w1, w2, w3 = i
        w1, w2, w3 = (w1//m, w1%m), (w2//m, w2%m), (w3//m, w3%m)

        count = 0
        for j in (w1, w2, w3):
            if l[j[0]][j[1]] != 0:
                count += 1
        if count != 0:
            continue

        temp_l = copy.deepcopy(l)
        for j in (w1, w2, w3):
            temp_l[j[0]][j[1]] = 1

        q = deque()
        for i in b:
            q.append(i)

        dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for i in dxdy:
                dx, dy = x + i[0], y + i[1]
                if dx >= n or dx < 0 or dy >= m or dy < 0:
                    continue
                if temp_l[dx][dy] == 2 or temp_l[dx][dy] == 1:
                    continue
                temp_l[dx][dy] = 2
                q.append((dx, dy))

        count2 = 0
        for i in range(n):
            for j in range(m):
                if temp_l[i][j] == 0:
                    count2 += 1
        if max < count2:
            max = count2

    print(max)