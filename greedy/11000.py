import sys
from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    lecture = PriorityQueue()
    for i in range(n):
        s, t = map(int, sys.stdin.readline().split())
        lecture.put((s, t))

    result = 0
    temp_lecture = PriorityQueue()
    while lecture.qsize() != 0:
        result += 1
        last_finish_time = lecture.get()[1]
        for i in range(lecture.qsize()):
            s, t = lecture.get()
            if s >= last_finish_time:
                last_finish_time = t
            else:
                temp_lecture.put((s, t))
        if temp_lecture.qsize() != 0:
            result += 1
            last_finish_time = temp_lecture.get()[1]
            for i in range(temp_lecture.qsize()):
                s, t = temp_lecture.get()
                if s >= last_finish_time:
                    last_finish_time = t
                else:
                    lecture.put((s, t))
    print(result)



