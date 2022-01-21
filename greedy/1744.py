if __name__ == "__main__":
    n = int(input())
    num = [int(input()) for _ in range(n)]
    num.sort(reverse=True)
    plus_list = list()
    minus_list = list()
    zero_count = 0

    for i in num:
        if i > 0:
            plus_list.append(i)
        elif i < 0:
            minus_list.append(i)
        else:
            zero_count += 1
    plus_list.sort(reverse=True)
    minus_list.sort()

    result = 0
    while len(plus_list) > 1:
        num1 = plus_list.pop(0)
        num2 = plus_list.pop(0)
        if num1 > 1 and num2 > 1:
            result += num1*num2
        else:
            result += num1 + num2
    if len(plus_list) == 1:
        result += plus_list.pop()

    while len(minus_list) > 1:
        result += minus_list.pop(0) * minus_list.pop(0)
    if len(minus_list) == 1:
        if zero_count == 0:
            result += minus_list.pop()
    print(result)
