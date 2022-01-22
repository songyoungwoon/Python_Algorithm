if __name__ == "__main__":
    n = int(input())
    k = int(input())

    s = list(map(int, input().split()))
    s_set = set(s)
    s_list = list(s_set)
    s_list.sort()

    distance = list()
    for i in range(len(s_list) - 1):
        distance.append(s_list[i+1] - s_list[i])

    distance.sort()
    for i in range(k - 1):
        if len(distance) > 0:
            distance.pop()
    print(sum(distance))