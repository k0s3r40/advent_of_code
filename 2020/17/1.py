def get_neighbours(crd):
    neighbours = []
    rules = []
    for index, value in enumerate(crd):
        rules.append([value - 1, value, value + 1])

    for x in rules[0]:
        for y in rules[1]:
            for z in rules[2]:
                neighbours.append((x, y, z))

    neighbours = [i for i in neighbours if i != crd]
    neighbours = [i for i in neighbours if any([cc == i[index] for index, cc in enumerate(crd)])]

    return neighbours


def solve(data, r):
    for i in range(r):
        for k in list(data.keys()):
            active = 0
            neighbours = get_neighbours(k)
            for neighbour in neighbours:
                if data.get(neighbour, None) is None:
                    data[neighbour] = '.'

            for n in neighbours:
                if data[n] == '#':
                    active += 1

            if data[k] == '#':
                if active not in [2, 3]:
                    data[k] = '.'

            if data[k] == '.':
                if active == 3:
                    data[k] = '#'

    return (sum([1 for v in data.values() if v == '#']))


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
    faces = [tuple(i for i in d) for d in data]
    data = {}
    for x, value in enumerate(faces):
        for y, v in enumerate(value):
            data[(x, y, 0)] = v
    wrong = [
        304,
    ]
    ans = solve(data, 6)
    if ans in wrong:
        print('WRONG:', ans)
    else:
        print(ans)
