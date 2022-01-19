import sys
from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    card = PriorityQueue()
    result = 0

    for i in range(n):
        card.put(int(sys.stdin.readline().strip()))
    while card.qsize() > 1:
        sum = 0
        sum += card.get()
        sum += card.get()
        result += sum
        card.put(sum)

    print(result)

