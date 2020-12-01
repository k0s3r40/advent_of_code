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


def find_first_value(data, expected_res):
    last_result = 0
    i = 0
    while True:
        data[1] = i
        data[2] = 0
        # 19690720
        matrix = get_matrix(data.copy())
        result = solve(data.copy(), matrix)

        if result <= expected_res:
            last_result = result
        else:
            return last_result, i
        i += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i) for i in f.read().split(',')]
    expected_result = 19690720
    result, x = find_first_value(data.copy(), expected_result)
    y = expected_result - result
    print(100 * x + y)
