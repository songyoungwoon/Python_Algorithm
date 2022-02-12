from heapq import heappush, heappop
input = __import__('sys').stdin.readline
if __name__ == "__main__":
    n, x = map(int, input().split())
    pt = list(map(int, input().split()))
    total = sum(pt)

    def binary_search(n):
        left = 1
        right = n
        mid = (left + right) // 2

        while left <= right:
            best_case = mid * x
            if best_case < total:
                left = mid + 1
                mid = (left + right) // 2
                continue
            q = []
            for i in range(mid):
                heappush(q, pt[i])
            for i in range(mid, n):
                temp = heappop(q)
                temp += pt[i]
                heappush(q, temp)
            time = max(q)

            if time > x:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        print(right + 1)
    binary_search(n)
