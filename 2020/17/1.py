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
    return neighbours


def solve(data, r):
    valid_crds = set([k for k, v in data.items() if v == '#'])
    for i in range(r):
        temp_elements = {}
        temp_crds = set(valid_crds)
        for crd in list(valid_crds):
            active = 0
            for neighbour in get_neighbours(crd):
                if neighbour in valid_crds:
                    active += 1
                else:
                    if temp_elements.get(neighbour, None) is None:
                        temp_elements[neighbour] = 0
                    temp_elements[neighbour] += 1
            if active not in [2, 3]:
                temp_crds.discard(crd)

        for k, v in temp_elements.items():
            if v == 3:
                temp_crds.add(k)

        valid_crds = temp_crds
    return len(valid_crds)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
    faces = [tuple(i for i in d) for d in data]
    data = {}
    for x, value in enumerate(faces):
        for y, v in enumerate(value):
            data[(x, y, 0)] = v

    print("Part 1:",solve(data, 6))
