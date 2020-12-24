if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
        data = [i.replace(
            'nw', '0'
        ).replace(
            'sw', '2'
        ).replace(
            'se', '3'
        ).replace(
            'ne', '5'
        ).replace(
            'w', '1'
        ).replace(
            'e', '4'
        ) for i in data]
    neighbours_crds = (
        (-1, 1),
        (1, 1),
        (2, 0),
        (1, -1),
        (-1, -1),
        (-2, 0),
    )
    new_data = []
    for i in data:
        temp_i = []
        for x in i:
            if x == '0':  # nw
                temp_i.append((-1, 1))
            if x == '5':  # ne
                temp_i.append((1, 1))
            if x == '4':  # E
                temp_i.append((2, 0))
            if x == '3':  # se
                temp_i.append((1, -1))
            if x == '2':  # sw
                temp_i.append((-1, -1))
            if x == '1':  # w
                temp_i.append((-2, 0))

        new_data.append(temp_i)
    data = new_data

    mid = (0, 0)

    tiles_hit = {}
    black_tiles = 0
    for path in data:
        temp_mid = mid
        for crd in path:
            temp_mid = (temp_mid[0] + crd[0],
                        temp_mid[1] + crd[1])
        if temp_mid not in tiles_hit:
            tiles_hit[temp_mid] = 0
        tiles_hit[temp_mid] += 1


    def update_area():
        x = [k[0] for k in tiles_hit]
        y = [k[1] for k in tiles_hit]
        min_x = min(x)
        max_x = max(x)
        min_y = min(y)
        max_y = max(y)

        for x in range(min_x - 2, max_x + 2):
            for y in range(min_y - 2, max_y + 2):
                crd = (x, y)
                if crd not in tiles_hit:
                    tiles_hit[crd] = 0


    update_area()
    for day in range(0, 101):
        update_area()
        black_tiles = {k: v for k, v in tiles_hit.items() if v % 2 != 0}
        white_tiles = {k: v for k, v in tiles_hit.items() if v % 2 == 0}
        for k, v in black_tiles.items():
            white = 0
            black = 0
            neighbours = []
            for n in neighbours_crds:
                neighbours.append((k[0] + n[0], k[1] + n[1]))
            for n in neighbours:
                if n in black_tiles:
                    black += 1
                else:
                    white += 1
            if black == 0 or black > 2:
                tiles_hit[k] += 1

        for k, v in white_tiles.items():
            white = 0
            black = 0
            neighbours = []
            for n in neighbours_crds:
                neighbours.append((k[0] + n[0], k[1] + n[1]))
            for n in neighbours:
                if n in black_tiles:
                    black += 1
                else:
                    white += 1

            if black == 2:
                tiles_hit[k] += 1

        print('Day', day, len(black_tiles))
