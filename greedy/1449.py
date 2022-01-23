if __name__ =="__main__":
    n, l = map(int, input().split())
    leak = list(map(int, input().split()))
    leak.sort()

    result = 0
    start = 0
    for i in range(len(leak)):
        if leak[i] > start:
            result += 1
            start = leak[i] + l - 0.5
        elif leak[i] == start:
            result += 1
            start = leak[i] + l
    print(result)