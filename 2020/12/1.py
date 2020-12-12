def solve(data):
    coordinates = [(0, 0)]
    rotation = 0
    directions = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0),
    }
    directions['F'] = directions['E']

    for i in data:
        direction = i[0]
        value = i[1]
        if direction in ['R', 'L']:
            value = value * (-1 if direction == 'L' else 1)

            rotation += value

            rotations = {

                270: directions['N'],
                0: directions['E'],
                90: directions['S'],
                180: directions['W']
            }
            directions['F'] = rotations[rotation % 360]
            continue
        for i in range(value):
            x = coordinates[-1][0]
            y = coordinates[-1][1]
            x += (directions[direction][0]) * 1
            y += (directions[direction][1]) * 1
            coordinates.append((x, y))

    last = coordinates[-1]
    x = abs(last[0])
    y = abs(last[1])

    return sum([x, y])

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [(i[0], int(i[1:])) for i in f.read().split()]
    print("Part 1:", solve(data))

