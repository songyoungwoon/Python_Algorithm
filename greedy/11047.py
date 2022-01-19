if __name__ == "__main__":
    n, k = map(int, input().split())
    coin = list()
    result = 0

    for i in range(n):
        price = int(input())
        if price <= k:
            coin.append(price)
    coin.sort(reverse=True)

    for i in coin:
        result += k//i
        k -= (k//i)*i

    print(result)