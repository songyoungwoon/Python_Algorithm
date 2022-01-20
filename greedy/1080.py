if __name__ == "__main__":
    n, m = map(int, input().split())
    nm1 = list(list(input()) for _ in range(n))
    nm2 = list(list(input()) for _ in range(n))

    result = 0
    dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(n):
        for j in range(m):
            if (i - 1) < 0 or (j - 1) < 0 or (i + 1) >= n or (j + 1) >= m:
                continue
            else:
                if nm1[i - 1][j - 1] != nm2[i - 1][j - 1]:
                    for d in dxdy:
                        di, dj = i + d[0], j + d[1]
                        if nm1[di][dj] == '0':
                            nm1[di][dj] = '1'
                        else:
                            nm1[di][dj] = '0'
                    result += 1
                else:
                    continue

    if nm1 == nm2:
        print(result)
    else:
        print(-1)
