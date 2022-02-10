input = __import__('sys').stdin.readline
if __name__ == "__main__":
    k, n = map(int, input().split())
    l = [int(input()) for _ in range(k)]
    def binary_search(n):
        left = 1
        right = 2**31 - 1
        mid = (left + right) // 2

        while left <= right:
            sum = 0
            for i in l:
                sum += i // mid
            if sum >= n:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        print(left-1)
    binary_search(n)