def solve_1(data):
    my_ts = data['my_ts']
    schedule = {}
    i = 0
    while True:
        schedule[i] = {}
        for x in data['bus_data']:
            if i % x == 0:
                schedule[i][x] = 'D'
                if i > my_ts:
                    return (i - my_ts) * x

            else:
                schedule[i][x] = '-'
        i += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i for i in f.read().split()]

    d = {'my_ts': int(data[0]),
         'bus_data': [int(i) for i in data[1].split(',') if i != 'x']}
    print('Part 1:', solve_1(d))
