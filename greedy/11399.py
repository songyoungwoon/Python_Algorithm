if __name__ == "__main__":
    n = input()
    P = list(map(int, input().split()))
    P.sort()
    wait_time = 0
    result = 0
    for i in P:
        result += wait_time + i
        wait_time += i

    print(result)
