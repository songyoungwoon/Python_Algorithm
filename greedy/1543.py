if __name__ == "__main__":
    str = input()
    word = input()

    result = 0
    word_len = len(word)
    start = 0
    end = word_len
    while end <= len(str):
        if str[start:end] == word:
            result += 1
            start = end
            end = start + word_len
        else:
            start += 1
            end += 1

    print(result)