def solve_1(data):
    my_ts = data['my_ts']
    schedule = {}
    i = 0
    part_1_solved = False
    while True:
        schedule[i] = {}
        for k, x in data['bus_data'].items():
            if x != 'x':
                x = int(x)
                if i % x == 0:
                    schedule[i][(k, x)] = 'D'
                    if i > my_ts and part_1_solved is False:
                        print('Part 1', (i - my_ts) * x)
                        part_1_solved = True
                else:
                    schedule[i][(k, x)] = '-'
            else:
                schedule[i][(k, x)] = '-'

        if i > len(data['bus_data']):
            consecutive = 0
            r = range((i + 1) - len(data['bus_data']), i + 1)
            for index, z in enumerate(r):
                v = [v for k, v in schedule[z].items()][index]
                k = [k for k, v in schedule[z].items()][index]
                if 'x' in k:
                    consecutive += 1
                elif v == 'D':
                    consecutive += 1
            if consecutive == len(data['bus_data']):
                print('Part 2', (i + 1) - len(data['bus_data']))
                return
        try:
            del schedule[i - len(data['bus_data'])]
        except:
            pass
        i += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i for i in f.read().split()]

    d = {'my_ts': int(data[0]),
         'bus_data': {index: i for index, i in enumerate(data[1].split(','))}}
    solve_1(d)
