import sys

def modpow(x, y):
    p = x
    ret = 1
    while y:
        if y % 2:
            ret = (ret * p) % mod
        p = (p * p) % mod
        y //= 2

    return ret

if __name__ == "__main__":
    m = int(sys.stdin.readline())
    mod = int(1e9 + 7)
    max_n = 4*(int(1e6) + 1)
    f = [1] * max_n
    for i in range(1, max_n):
        f[i] = (f[i-1]*i) % mod
    for i in range(m):
        n, k = map(int, sys.stdin.readline().split())
        a = f[n]
        b = (f[k] * f[n - k]) % mod

        b = modpow(b, mod - 2)
        print((a * b) % mod)
