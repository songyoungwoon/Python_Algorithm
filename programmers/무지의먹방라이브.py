import copy

def solution(food_times, k):
    answer = 0
    length = len(food_times)
    idx = range(length)
    while k > 0:
        idx2 = []
        max_height, k = k//length, k%length
        if k != 0 and max_height == 0:
            return idx[k]+1
        for i in idx:
            fti = food_times[i]
            if fti <= max_height:
                k += max_height - fti
                food_times[i] = 0
            else:
                food_times[i] -= max_height
                idx2.append(i)
        length = len(idx2)
        idx = copy.deepcopy(idx2)
        if length == 0:
            return -1
    answer = idx[0]+1
    return answer