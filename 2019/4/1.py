def check_digit(d):
    d = str(d)
    for index, value in enumerate(d):
        if index + 1 < len(d) - 1:
            if d[index + 1] < d[index]:
                return 0
        else:
            if d[index] < d[index - 1]:
                return 0

    return 1

def check_adjacent(lst):
    for index, value in enumerate(lst):
        print(value)

def solve(x, y):
    possible = 0
    poss = []
    for i in range(x, y):
        possible += check_digit(i)
        if check_digit(i) == 1:
            poss.append(i)
    print(poss[:10])
    return possible


# not 2099
# not 331435
# not 282347
# not 1041
# not 129608
if __name__ == '__main__':
    for i in [128888, 128889, 128899, 128999, 129999, 133333, 133334, 133335, 133336, 133337]:
        check_adjacent(str(i))
        print('----')
    # print(solve(128392, 643281))
