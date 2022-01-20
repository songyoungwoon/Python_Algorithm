if __name__ == "__main__":
    n = int(input())
    w = list(map(int, input().split()))
    w.sort()

    result = 0
    for i in range(n):
        if result + 1 >= w[i]:
            result += w[i]
        else:
            break

    print(result+1)





