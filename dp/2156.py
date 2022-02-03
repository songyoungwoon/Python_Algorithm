import sys

if __name__ == "__main__":
    n = int(input())
    grape = [int(sys.stdin.readline()) for _ in range(n)]
    grape.insert(0, 0)

    if n == 1:
        print(grape[1])
        exit()

    dp_in = [0 for _ in range(n + 1)]
    dp_inin = [0 for _ in range(n + 1)]
    dp_out = [0 for _ in range(n + 1)]

    dp_in[1] = grape[1]
    dp_inin[1] = grape[1]
    dp_inin[2] = grape[1] + grape[2]
    dp_out[1] = 0
    for i in range(2, n + 1):
        dp_in[i] = grape[i] + dp_out[i - 1]
        dp_inin[i] = grape[i] + dp_in[i - 1]
        dp_out[i] = max(dp_in[i - 1], dp_inin[i - 1], dp_out[i - 1])

    print(max(dp_out[n], dp_in[n], dp_inin[n]))

