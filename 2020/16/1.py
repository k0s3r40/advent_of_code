def solve(my_ticket, rules, nearby_tickets):
    invalid_nums = []
    invalid_tickets = []
    for index, ticket in enumerate(nearby_tickets):
        for num_index, num in enumerate(ticket):
            valid = False
            for k, v in rules.items():
                if v[0][0] <= num <= v[0][1] or v[1][0] <= num <= v[1][1]:
                    valid = True

            if valid is False:
                invalid_nums.append(num)
                invalid_tickets.append(index)
                continue

    d = {i: [] for i in range(len(my_ticket))}
    for k, v in rules.items():
        for i in range(len(my_ticket)):
            errors = 0
            for ticket in [i for index, i in enumerate(nearby_tickets) if index not in invalid_tickets] + [my_ticket]:
                num = ticket[i]
                if v[0][0] <= num <= v[0][1] or v[1][0] <= num <= v[1][1]:
                    pass
                else:
                    errors += 1
            if errors == 0:
                d[i].append(k)
    removed = []
    sure = {}
    i = 1000
    while d != {} or i < 1000:
        for key in list(d.keys()):
            d[key] = [i for i in d[key] if i not in removed]

            if len(d[key]) == 1:
                sure[key] = d[key][0]
                removed.append(d[key][0])
                del d[key]
        i+=1

    part_2 = 1
    for k, v in sure.items():
        if v.split(' ')[0] == 'departure':
            part_2 *= my_ticket[k]


    print('Part 1:', sum(invalid_nums))
    print('Part 2:', part_2)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')

    my_ticket = [int(i) for i in data[1].split(':')[1].strip('\n').split(',')]

    rules = {i.split(':')[0].strip(): [
        (int(i.split(':')[1].strip().split('or')[0].strip().split('-')[0]),
         int(i.split(':')[1].strip().split('or')[0].strip().split('-')[1])),

        (int(i.split(':')[1].strip().split('or')[1].strip().split('-')[0]),
         int(i.split(':')[1].strip().split('or')[1].strip().split('-')[1]))
    ] for i in data[0].split('\n')}

    nearby_tickets = [list(map(int, i.split(','))) for i in data[2].split(':')[1].strip('\n').split('\n')]
    solve(my_ticket, rules, nearby_tickets)
