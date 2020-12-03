import numpy
def solve(data, right, down):
    x_pos = 0
    trees = 0

    for index, i in enumerate(data):
        if index == 0:
            x_pos += right
        else:

            if down != 2 or index % down == 0:
                if i[x_pos] == '#':
                    trees += 1
                x_pos += right
    return trees

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i.split()[0] for i in f.readlines()]
        for x, v in enumerate(data):
            data[x] = [i for i in v * len(data)]
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    print('part1',solve(data, 3, 1))
    print('part2', numpy.prod([solve(data, i[0], i[1]) for i in slopes]))
