def solve(data, matrix):
    for i in matrix:
        if i[0] == 99:
            return data[0]
        if i[0] == 1:
            data[i[3]] = data[i[1]] + data[i[2]]
        if i[0] == 2:
            data[i[3]] = data[i[1]] * data[i[2]]
    return data[0]


def get_matrix(data):
    matrix = []
    secondary = []
    for index, i in enumerate(data):
        if index % 4 == 0:
            if secondary:
                matrix.append(secondary)
            secondary = []
        secondary.append(i)

    matrix.append(data[-4:])
    return matrix


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i) for i in f.read().split(',')]

    data[1] = 12
    data[2] = 2

    matrix = get_matrix(data)
    print(solve(data, matrix))
