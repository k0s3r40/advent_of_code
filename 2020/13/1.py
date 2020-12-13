"""
4,5  |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
3,3+1|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
2,3  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
1,2  |--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
0,1  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
     0123456789111111111122222222223333333333444444444455555555556666666666
               012345678901234567890123456789012345678901234567890123456789


The logic which should be implemented is
to find the biggest common divider between all of the bus_speeds + their indexes in the columns

"""


def solve(data):
    bus_data = [(index, value) for index, value in enumerate([int(v) if v != 'x' else 'x' for k, v in data['bus_data'].items()])]
    position = 0
    speed = 0
    my_ts = data['my_ts']
    bus_found = False
    while bus_found is False:
        for index, bus_speed in bus_data:
            if bus_speed != 'x':
                if my_ts % bus_speed == 0:
                    print('Part 1:', my_ts)
                    bus_found = True
        my_ts += 1

    for index, bus_speed in bus_data:
        if bus_speed != 'x':
            if index == 0:
                position = 0
                speed = bus_speed
                continue
            while (position + index) % bus_speed != 0:
                position += speed
            speed *= bus_speed

    for index, bus_speed in bus_data:
        if bus_speed != 'x':
            assert (position + index) % bus_speed == 0

    print('Part 2:', position)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i for i in f.read().split()]

    d = {'my_ts': int(data[0]),
         'bus_data': {index: i for index, i in enumerate(data[1].split(','))}}
    solve(d)
