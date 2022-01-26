from queue import PriorityQueue

if __name__ == "__main__":
    n, m = map(int, input().split())
    card_list = list(map(int, input().split()))
    card_que = PriorityQueue()

    for i in card_list:
        card_que.put(i)

    for i in range(m):
        two_sum = card_que.get() + card_que.get()
        card_que.put(two_sum)
        card_que.put(two_sum)
    sum = 0
    while card_que.qsize() != 0:
        sum += card_que.get()
    print(sum)
