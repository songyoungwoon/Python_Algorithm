if __name__ == "__main__":
    n, k = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(n)]
    item.insert(0,[0,0])
    dp_value = [[0]*(k+1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if item[i][0] <= j:
                dp_value[i][j] = max(dp_value[i-1][j], item[i][1] + dp_value[i - 1][j - item[i][0]])
            else:
                dp_value[i][j] = dp_value[i-1][j]

    print(dp_value[n][k])
