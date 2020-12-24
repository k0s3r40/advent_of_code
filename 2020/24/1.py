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

    tiles_hit = []
    black_tiles = 0
    for path in data:
        temp_mid = mid
        for crd in path:
            temp_mid = (temp_mid[0] + crd[0],
                        temp_mid[1] + crd[1])
        if temp_mid not in tiles_hit:
            tiles_hit.append(temp_mid)
            black_tiles += 1
        else:
            tiles_hit.remove(temp_mid)
            black_tiles -= 1
    print(black_tiles)
