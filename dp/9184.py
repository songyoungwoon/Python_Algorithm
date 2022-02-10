import sys
if __name__ == "__main__":
    N = 21
    w = [[[0]*(N) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for z in range(N):
                if i == 0 or j == 0 or z == 0:
                    w[i][j][z] = 1
                    continue
                if i < j and j < z:
                    w[i][j][z] = w[i][j][z-1] + w[i][j-1][z-1] - w[i][j-1][z]
                else:
                    w[i][j][z] = w[i-1][j][z] + w[i-1][j-1][z] + w[i-1][j][z-1] - w[i-1][j-1][z-1]

    while True:
        a, b, c = map(int, sys.stdin.readline().split())
        if a == -1 and b == -1 and c == -1:
            break
        if a <= 0 or b <= 0 or c <= 0:
            print(f'w({a}, {b}, {c}) = 1')
        elif a > 20 or b > 20 or c > 20:
            print(f'w({a}, {b}, {c}) = {w[20][20][20]}')
        else:
            print(f'w({a}, {b}, {c}) = {w[a][b][c]}')

