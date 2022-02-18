input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    for i in range(n):
        print(a[i])