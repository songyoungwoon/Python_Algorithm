if __name__ == "__main__":
    str = input()
    str += '/'
    sum_str = ''
    sum = 0
    isminusTrue = False
    for i in range(len(str)):
        if str[i].isdigit():
            sum_str += str[i]
        else:
            if isminusTrue == False:
                sum += int(sum_str)
                sum_str = ''
            else :
                sum -= int(sum_str)
                sum_str = ''
        if str[i] == '-':
            isminusTrue = True
    print(sum)