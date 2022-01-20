import sys

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        applicant = list()
        result = 0
        for j in range(n):
            dg, ig = map(int, sys.stdin.readline().split())
            applicant.append((dg, ig))
        applicant.sort(key=lambda x:x[0])

        min_ig = applicant[0][1]
        result += 1
        for j in range(1, n):
            if applicant[j][1] < min_ig:
                result += 1
                min_ig = applicant[j][1]
        print(result)
