input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, c = map(int, input().split())
    x = [int(input()) for _ in range(n)]
    x.sort()
    def binary_search(c):
        left = 1
        right = int(1e9)
        mid = (left + right) // 2

        while left <= right:
            start = 0
            sum = 1
            for i in range(1, len(x)):
                if i <= start:
                    continue
                if x[i] - x[start] >= mid:
                    sum += 1
                    start = i
            if sum >= c:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        print(left - 1)

    binary_search(c)
