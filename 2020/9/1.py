def solve_part1(data):
    preamble = 25
    part_1 = 0
    for index, value in enumerate(data):
        if index >= preamble:
            found = False
            chunk = data[(index) - preamble:index]
            for x in chunk:
                if value - x in chunk:
                    found = True
            if found is False:
                part_1 = value
                break

    weakness = part_1
    preamble = 1
    while True:
        for index, value in enumerate(data):
            if index >= preamble:
                chunk = data[(index) - preamble:index]
                if len(chunk) > 1 and sum(chunk) == weakness:
                    return part_1, (min(chunk) + max(chunk))
        preamble += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [int(i) for i in f.read().split()]
    answer = solve_part1(data)
    for i, v in enumerate(answer):
        print(f'part {i + 1}: {v}')
