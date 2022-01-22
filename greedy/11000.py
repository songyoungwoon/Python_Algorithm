import sys
from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    lecture = list()
    for i in range(n):
        s, t = map(int, sys.stdin.readline().split())
        lecture.append((s, t))
    lecture.sort(key=lambda x:(x[1], x[0]))
    result = 0
    temp_lecture = list()
    while len(lecture) != 0:
        result += 1
        last_finish_time = lecture.pop(0)[1]
        for i in range(len(lecture)):
            s, t = lecture.pop(0)
            if s >= last_finish_time:
                last_finish_time = t
            else:
                temp_lecture.append((s, t))
        if len(temp_lecture) != 0:
            result += 1
            last_finish_time = temp_lecture.pop(0)[1]
            for i in range(len(temp_lecture)):
                s, t = temp_lecture.pop(0)
                if s >= last_finish_time:
                    last_finish_time = t
                else:
                    lecture.append((s, t))
    print(result)



