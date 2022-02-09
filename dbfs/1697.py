from queue import Queue

if __name__ == "__main__":
    n, k = map(int, input().split())

    q = Queue()
    q2 = Queue()
    q.put((k, 0))
    result = 0
    while q.qsize() != 0:
        while q.qsize() != 0:
            v, count = q.get()
            if v == n:
                print(count)
                exit()
            if v < n:
                q2.put((v + 1, count + 1))
                continue
            if v % 2 == 0:
                q2.put((v / 2, count + 1))
            q2.put((v - 1, count + 1))
            q2.put((v + 1, count + 1))
        while q2.qsize() != 0:
            v, count = q2.get()
            if v == k:
                print(count)
                exit()
            if v < n:
                q.put((v + 1, count + 1))
                continue
            if v % 2 == 0:
                q.put((v / 2, count + 1))
            q.put((v - 1, count + 1))
            q.put((v + 1, count + 1))


