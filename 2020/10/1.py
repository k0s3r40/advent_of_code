def solve_part_1(data):
    arr = list()
    for index, value in enumerate(data):
        if index < len(data) - 1:
            arr.append(data[index + 1] - value)
    d = {i: arr.count(i) + 1 for i in set(arr)}

    iterations = {0: 1}

    for i in data:
        if not iterations.get(i, None):
            iterations[i] = 0
        iterations[i] += iterations.get(i - 1, 0) + iterations.get(i - 2, 0) + iterations.get(i - 3, 0)
    print(iterations)
    return {'part 1': d[1] * d[3], 'part 2': iterations[data[-1]]}


if __name__ == '__main__':
    with open('input.txt') as f:
        data = sorted([int(i) for i in f.read().split()])

    for k, v in solve_part_1(data).items():
        print(k, v)
