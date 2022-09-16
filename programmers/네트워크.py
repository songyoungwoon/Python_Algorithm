from collections import deque


def solution(n, computers):
    answer = 0
    visit = [False for i in range(n)]

    for i in range(n):
        if visit[i] == True:
            continue
        visit[i] = True
        q = deque()
        q.append(i)
        while q:
            k = q.pop()
            for j in range(len(computers[k])):
                if computers[k][j] == 1 and visit[j] == False:
                    print(j)
                    q.append(j)
                    visit[j] = True
        answer += 1
    return answer