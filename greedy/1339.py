if __name__ == "__main__":
    n = int(input())
    alpha = {}
    result = 0
    for i in range(n):
        word = input()
        max_len = len(word)
        for j in range(len(word)):
            try:
                alpha[word[j]] += 10**(max_len - j - 1)
            except KeyError:
                alpha[word[j]] = 10**(max_len - j - 1)

    sort_alpha = sorted(alpha.items(), key=lambda x:x[1], reverse=True)
    start = 9
    for i in sort_alpha:
        result += i[1] * start
        start -= 1

    print(result)


