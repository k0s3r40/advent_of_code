def solve_part_1(data):
    indexes_passed = []
    acc = 0
    index = 0
    while True:
        if index not in indexes_passed:
            indexes_passed.append(index)
        else:
            return acc
        action, inc = data[index][0], int(data[index][1])
        if action == 'acc':
            acc += inc
        if action == 'jmp':
            index += inc
        else:
            index += 1


def solve_part_2(data):
    indexes_passed = []
    acc = 0
    index = 1
    while True:
        if index not in indexes_passed:
            indexes_passed.append(index)
        else:
            return None
        action, inc = data[index-1][0], int(data[index-1][1])
        if action == 'acc':
            acc += inc
            if index == len(data) - 1:
                return acc
        if action == 'jmp':
            index += inc
        else:
            index += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i.split(' ') for i in f.read().split('\n')]

    print('part 1:', solve_part_1(data))

    jumps = [(index, i) for index, i in enumerate(data) if i[0] == 'jmp']
    nones = [(index, i) for index, i in enumerate(data) if i[0] == 'nop']

    solves = []
    for i in jumps:
        index = i[0]
        with open('input.txt') as f:
            data = [i.split(' ') for i in f.read().split('\n')]
        i[1][0] = 'nop'
        data[index] = i[1]
        answer = solve_part_2(data)
        if answer:
            solves.append(answer)

    for i in nones:
        index = i[0]
        with open('input.txt') as f:
            data = [i.split(' ') for i in f.read().split('\n')]
        i[1][0] = 'jmp'
        data[index] = i[1]
        answer = solve_part_2(data)
        if answer:
            solves.append(answer)
    print('part 2:', solves[0])

