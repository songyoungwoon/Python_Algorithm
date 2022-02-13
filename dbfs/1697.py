from collections import deque

if __name__ == "__main__":
    n, k = map(int, input().split())

    q = deque()
    q.append((0, n))
    visit = [False]*100001
    while q:
        count, now = q.popleft()
        if visit[now] == True:
            continue
        visit[now] = True
        if now == k:
            print(count)
            exit()
        for i in [now*2, now - 1, now + 1]:
            if i < 0 or i > 100000:
                continue
            q.append((count + 1, i))