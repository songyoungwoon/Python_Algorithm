input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n = list(input())
    n.pop()
    n = list(map(int, n))
    n.sort(reverse=True)
    n = list(map(str, n))
    print("".join(n))