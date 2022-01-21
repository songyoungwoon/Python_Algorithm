if __name__ == "__main__":
    str = input()
    zero_list = list()
    one_list = list()

    str += '/'
    start_word = str[0]
    start = 0
    end = 0
    for i in str:
        if i == start_word:
            end += 1
        else:
            if start_word == '0':
                zero_list.append(str[start:end])
            else:
                one_list.append(str[start:end])
            start = end
            end += 1
            start_word = str[start]

    print(min(len(zero_list), len(one_list)))

