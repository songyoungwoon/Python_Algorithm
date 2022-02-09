from queue import Queue

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    c = [[] for _ in range(n + 1)]
    for i in range(k):
        v, e = map(int, input().split())
        c[v].append(e)
        c[e].append(v)

    q = Queue()
    q.put(c[1])
    s = set()
    s.add(1)
    count = 0
    while q.qsize() != 0:
        node = q.get()
        for i in node:
            if s.__contains__(i):
                continue
            q.put(c[i])
            s.add(i)
            count += 1
    print(count)