def solve_1(data, d):
    i = len(data) + 1
    last = data[-1]
    while i <= 2020:
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
    print('Part 1:', last)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(value) for value in f.read().split(',')]
    d = {}
    for index, i in enumerate(data, start=1):
        if d.get(i, None) is None:
            d[i] = [index]
        else:
            d[i].append(index)

    solve_1(data, d)
