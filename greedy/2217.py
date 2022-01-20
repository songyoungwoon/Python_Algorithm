if __name__ == "__main__":
    n = int(input())
    w = [int(input()) for _ in range(n)]
    w.sort(reverse=True)

    count = 0
    result = 0
    for i in range(n):
        if w[i]*(count+1) > result:
            result = w[i]*(count+1)
            count += 1
        else : count += 1

    print(result)
