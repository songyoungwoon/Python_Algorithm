def solution(brown, yellow):
    answer = []
    n = brown + yellow
    for h in range(3, n // 3 + 1):
        if n % h != 0:
            continue
        w = n // h
        border = h * 2 + (w - 2) * 2
        if (n - border) == yellow:
            print(h)
            return w, h
    return answer