input = __import__('sys').stdin.readline

if __name__ == "__main__":
    n, r, c = map(int, input().split())

    lineNum = r + c - 1
    pre_line_count = 0
    for i in range(lineNum):
        if i <= n:
            pre_line_count += i
        if i > n :
            pre_line_count += n - (i - n)

    if lineNum <= n:
        if lineNum % 2 == 0:
            pre_line_count += r
        else:
            pre_line_count += n - r + 1 - (n - lineNum)
    else:
        if lineNum % 2 == 0:
            pre_line_count += r - (lineNum - n)
        else:
            pre_line_count += n - r + 1
    print(pre_line_count)