from collections import deque


def solution(n, wires):
    answer = 100
    len_wires = len(wires)
    for i in range(len_wires):
        graph = [[] for _ in range(n + 1)]
        visit = [False for _ in range(n + 1)]
        for j in range(len_wires):
            if i == j:
                continue
            u, v = wires[j]
            graph[u].append(v)
            graph[v].append(u)
        node_count = 0
        q = deque()
        q.append(1)
        while q:
            k = q.pop()
            if visit[k] == False:
                node_count += 1
            visit[k] = True
            for j in graph[k]:
                if visit[j] == False:
                    q.append(j)
        answer = min(answer, abs(node_count - (n - node_count)))

    return answer