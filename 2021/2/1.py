def replace_values(data):
    return [i for i in data]


def solve_1(data):
    x = 0
    y = 0
    for i in data:
        k, v = i.split(' ')
        v = int(v)
        if k in ['up', 'down']:
            multiplier = -1 if k[0] == 'u' else 1
            y += v * multiplier
        else:
            x += v
    return x * y


def solve_2(data):
    x = 0
    y = 0
    aim = 0
    for i in data:
        k, v = i.split(' ')
        v = int(v)
        if k in ['up', 'down']:
            multiplier = -1 if k[0] == 'u' else 1
            if multiplier == 1:
                aim += v
            else:
                aim -= v
        else:
            x += v
            y += aim * v
    return x * y


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i for i in f.readlines()]
    print(f'Part 1: {solve_1(data)}')
    print(f'Part 2: {solve_2(data)}')
