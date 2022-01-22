if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        w = list(map(int, input().split()))
        w.sort()

        fw = list()
        bw = list()
        for j in range(int(len(w)/2 + 1)):
            if len(w) > 0:
                fw.append(w.pop(0))
            if len(w) > 0:
                bw.insert(0, w.pop(0))
        fw += bw
        distance = list()
        distance.append(abs(fw[0] - fw[len(fw) - 1]))
        for j in range(len(fw) - 1):
            distance.append(abs(fw[j + 1] - fw[j]))
        print(max(distance))