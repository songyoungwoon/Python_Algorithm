from queue import Queue

if __name__ == "__main__":
    n, k = map(int, input().split())

    q = Queue()
    q.put((0, n))
    while not q.empty():
        count, now = q.get()
        if now < 0 or now > 100000:
            continue
        if now == k:
            print(count)
            exit()
        q.put((count + 1, now * 2))
        q.put((count + 1, now - 1))
        q.put((count + 1, now + 1))








