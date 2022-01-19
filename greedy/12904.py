if __name__ == "__main__":
    s = input()
    t = input()
    result = 0

    l = len(t) - len(s)
    for i in range(l):
        if t[len(t)- 1] =='A':
            t = t[0:len(t)-1]
        elif t[len(t)-1] == 'B':
            t = "".join(reversed(t[0:len(t)-1]))

    if s == t:
        print(1)
    else: print(0)




