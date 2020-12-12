from math import sin, cos, radians


def solve(data):
    coordinates = [(0, 0)]
    waypoint = [(10, 1)]
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
            last_waypoint = waypoint[-1]

            ox, oy = (0, 0)

            px, py = last_waypoint

            angle = radians(value)*-1

            qx = ox + cos(angle) * (px - ox) - sin(angle) * (py - oy)
            qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)
            crds = (round(qx), round(qy))
            waypoint.append(crds)

            continue
        elif direction == 'F':
            for i in range(value):
                x = coordinates[-1][0]
                y = coordinates[-1][1]
                x += waypoint[-1][0]
                y += waypoint[-1][1]
                coordinates.append((x, y))
        else:
            for i in range(value):
                x = waypoint[-1][0]
                y = waypoint[-1][1]
                x += (directions[direction][0])
                y += (directions[direction][1])
                waypoint.append((x, y))

    last = coordinates[-1]
    x = abs(last[0])
    y = abs(last[1])

    return sum([x, y])


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [(i[0], int(i[1:])) for i in f.read().split()]
    print("Part 2:", solve(data))
