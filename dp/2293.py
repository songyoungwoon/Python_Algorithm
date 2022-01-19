if __name__ == "__main__":
    n, k = map(int, input().split())
    coin = list()
    result = [0 for i in range(k+1)]

    for i in range(n):
        price = int(input())
        if price <= k:
            coin.append(price)

    for i in range(len(coin)):
        for j in range(k+1):
            if i == 0:
                if j % coin[i] == 0:
                    result[j] = 1
            elif j//coin[i] > 0:
                result[j] += result[j - coin[i]]

    print(result[k])