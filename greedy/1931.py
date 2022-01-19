if __name__ == "__main__":
    n = int(input())
    time = list()
    result = 0
    finish_time = 0

    for i in range(n):
        s, f = map(int, input().split())
        time.append((s,f))

    time.sort(key=lambda x:(x[1],x[0]))
    for i in time:
        if i[0] >= finish_time:
            result += 1
            finish_time = i[1]

    print(result)
