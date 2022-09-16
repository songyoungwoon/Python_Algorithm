def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    i = 0
    j = 1
    while j < len(routes):
        stand = routes[i][1]
        compare = routes[j][0]
        if compare > stand:
            i = j
            j = i + 1
            answer += 1
        else:
            j += 1
        if j == len(routes):
            answer += 1
            break

    return answer