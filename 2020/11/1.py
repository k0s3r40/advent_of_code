def solve_part_1(d, iterations=0, seated=0):
    d_temp = {**d}

    arr = []
    for k, v in d.items():
        arr.append(v)
        if len(arr) > 9:
            print(''.join(arr))
            arr = []
    print('----------')
    for k, v in d.items():
        if iterations == 0:
            if v != '.':
                d_temp[k] = '#'
        else:
            indexes = [(k[0] + 1, k[1]),
                       (k[0] - 1, k[1]),
                       (k[0], k[1] + 1),
                       (k[0], k[1] - 1),
                       (k[0] + 1, k[1] - 1),
                       (k[0] - 1, k[1] - 1),
                       (k[0] + 1, k[1] + 1),
                       (k[0] - 1, k[1] + 1),
                       ]
            if v == 'L':
                occ = 0
                for index in indexes:
                    if d.get(index, None):
                        if d[index] == '#':
                            occ += 1

                if occ == 0:
                    d_temp[k] = '#'

            if v == '#':
                occ = 0
                for index in indexes:
                    if d.get(index, None):
                        if d[index] == '#':
                            occ += 1
                if occ >= 4:
                    d_temp[k] = 'L'

    iterations += 1

    seated_temp = 0
    for k, v in d_temp.items():
        if v == '#':
            seated_temp += 1
    if seated_temp == seated:
        print('part 1:', seated_temp)
        return

    d = {**d_temp}
    solve_part_1(d, iterations, seated_temp)

def solve_part_2(d, iterations=0, seated=0):
    d_temp = {**d}

    arr = []
    for k, v in d.items():
        arr.append(v)
        if len(arr) > 9:
            print(''.join(arr))
            arr = []
    print('----------')
    for k, v in d.items():
        if iterations == 0:
            if v != '.':
                d_temp[k] = '#'
        else:
            indexes = [(k[0] + 1, k[1]),
                       (k[0] - 1, k[1]),
                       (k[0], k[1] + 1),
                       (k[0], k[1] - 1),
                       (k[0] + 1, k[1] - 1),
                       (k[0] - 1, k[1] - 1),
                       (k[0] + 1, k[1] + 1),
                       (k[0] - 1, k[1] + 1),
                       ]
            if v == 'L':
                occ = 0
                for index in indexes:
                    if d.get(index, None):
                        if d[index] == '#':
                            occ += 1

                if occ == 0:
                    d_temp[k] = '#'

            if v == '#':
                occ = 0
                for index in indexes:
                    if d.get(index, None):
                        if d[index] == '#':
                            occ += 1
                if occ >= 4:
                    d_temp[k] = 'L'

    iterations += 1
    if iterations == 3:
        return
    seated_temp = 0
    for k, v in d_temp.items():
        if v == '#':
            seated_temp += 1
    if seated_temp == seated:
        print('part 2:', seated_temp)
        return

    d = {**d_temp}
    solve_part_2(d, iterations, seated_temp)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i for i in f.read().split()]
    d = {}
    for i_y, row in enumerate(data):
        for i_x, value in enumerate(row):
            d[(i_y, i_x)] = value
    # solve_part_1(d)
    solve_part_2(d)

    # solve_part_1(data)
