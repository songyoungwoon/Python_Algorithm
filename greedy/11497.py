if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        w = list(map(int, input().split()))
        w.sort()

        distance = list()
        distance.append(abs(w[0] - w[1]))
        distance.append(abs(w[len(w) - 1] - w[len(w) - 2]))
        for j in range(len(w) - 2):
            distance.append(abs(w[j] - w[j + 2]))
        print(max(distance))