if __name__ == "__main__":
    n, m = map(int, input().split())

    location = list(map(int, input().split()))
    location.sort()
    reverse_location = sorted(location, reverse=True)

    result = -max(abs(location[0]), abs(location[len(location) - 1]))
    for i in range(len(location)):
        if location[i] < 0:
            if i % m == 0:
                result += abs(location[i]*2)
        if location[i] > 0:
            break

    for i in range(len(reverse_location)):
        if reverse_location[i] > 0:
            if i % m == 0:
                result += abs(reverse_location[i]*2)
        if reverse_location[i] < 0:
            break

    print(result)





