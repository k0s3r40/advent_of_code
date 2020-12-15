import datetime


def solve_1(data, r):
    d = {i: [] for i in range(r + 1)}
    for index, x in enumerate(data, start=1):
        d[x] = [index, index]

    start = len(data) + 1
    last = data[-1]
    now = datetime.datetime.now()
    for i in list(d.keys())[start:]:
        next_num = d[last][1] - d[last][0]
        if d[next_num] == []:
            d[next_num] = [i]
        d[next_num] = [d[next_num][-1], i]
        last = next_num
    print(datetime.datetime.now() - now)
    return last


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(value) for value in f.read().split(',')]

    print('Part 1:', solve_1(data, 2020))

    print('Part 2:', solve_1(data, 30000000))
