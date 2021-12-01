def solve_1(data):
    counter = 0
    for index, value in enumerate(data):
        if (index + 1 < len(data)) and data[index + 1] > value:
            counter += 1
    return counter


def solve_2(data):
    groups = [sum([data[index + i] for i in range(3) if index + 2 < len(data)]) for index, _ in enumerate(data)]
    return solve_1(groups)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i) for i in f.readlines()]
    print(f'Part 1: {solve_1(data)}')
    print(f'Part 2: {solve_2(data)}')
