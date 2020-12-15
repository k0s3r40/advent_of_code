def solve_1(data, r):
    d = {i: [] for i in range(r + 1)}
    for index, x in enumerate(data, start=1):
        d[x].append(index)
    start = len(data) + 1
    last = data[-1]
    print(last)
    for i in list(d.keys())[start:]:
        if len(d[last]) == 1:
            next_digit = 0
        else:
            next_digit = last
            next_digit = d[next_digit][1] - d[next_digit][0]
        if len(d[next_digit]) == 0:
            d[next_digit] = [i]
        else:
            d[next_digit] = (d[next_digit][-1], i)
        last = next_digit
    return last


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(value) for value in f.read().split(',')]

    print('Part 1:', solve_1(data, 2020))

    # print('Part 2:', solve_1(data, 30000000))
