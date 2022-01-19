if __name__ == "__main__":
    n = int(input())
    max_date = 0
    homework = []
    for i in range(n):
        d, w = map(int, input().split())
        homework.append((d, w))
        if max_date < d :
            max_date = d
    clear_homework = [0 for i in range(max_date+1)]

    homework.sort(key=lambda x:x[1], reverse=True)
    for i in homework:
        d, w = i[0], i[1]
        for i in range(d, 0, -1):
            if clear_homework[i] == 0:
                clear_homework[i] = w
                break

    print(sum(clear_homework))
