def solve_1(data, d, r):
    i = len(data) + 1
    last = data[-1]
    while i <= r:
        if len(d[last]) <= 1:
            next_digit = 0
        else:
            next_digit = last
            next_digit = d[next_digit][1] - d[next_digit][0]
        if d.get(next_digit, None) is None:
            d[next_digit] = [i]
        else:
            d[next_digit].append(i)
            d[next_digit] = d[next_digit][-2:]

        last = next_digit

        i += 1
    return last


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(value) for value in f.read().split(',')]
    d = {}
    for index, i in enumerate(data, start=1):
        if d.get(i, None) is None:
            d[i] = [index]
        else:
            d[i].append(index)

    print('Part 1:', solve_1(data, d, 2020))

    d = {}
    for index, i in enumerate(data, start=1):
        if d.get(i, None) is None:
            d[i] = [index]
        else:
            d[i].append(index)

    print('Part 2:', solve_1(data, d, 30000000))
