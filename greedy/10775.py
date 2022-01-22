import sys

if __name__ == "__main__":
    g = int(input())
    p = int(input())
    g_set = set()
    g_dict = dict()

    for i in range(p):
        g = int(sys.stdin.readline())
        g_set.add(g)
        try:
            g_dict[g] += 1
        except KeyError:
            g_dict[g] = 1

    g_list = sorted(list(g_set))
    start = 1
    result = 0
    for i in g_list:
        if g_dict[i] < i - start + 1:
            result += g_dict[i]
            start += g_dict[i]
        else:
            result += i - start + 1
            start = i + 1
    print(result)

