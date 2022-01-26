import time
def upper_word():
    word = 'ABcaasfadfa'*10000000
    start = time.time()
    first = word[0]
    remain = word[1:]
    upper = remain.upper()
    lower = remain.lower()
    '''
    l = len(word)
    upper_count = 0
    for i in range(l):
        if word[i].isupper():
            upper_count += 1

    if upper_count == 1:
        if word[0].isupper():
            print(time.time() - start)
            return True
        else:
            print(time.time() - start)
            return False
    elif upper_count > 0:
        if upper_count == l:
            print(time.time() - start)
            return True
        else:
            print(time.time() - start)
            return False
    else:
        print(time.time() - start)
        return True
upper_word()
'''
    if first.isupper() :
        if remain == upper or remain == lower:
            print(time.time() - start)
            return True
        else:
            print(time.time() - start)
            return False
    else:
        if remain == lower:
            print(time.time() - start)
            return True
        else:
            print(time.time() - start)
            return False
upper_word()
