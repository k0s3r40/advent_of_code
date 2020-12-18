def solve_1(data):
    ans = 0
    d = {}

    while True:
        forbidden_indexes = []
        ok = False
        for index, i in enumerate(data):
            if index % 2 == 1:
                if i == '+' and ok is False:
                    d[(index - 1, index + 1)] = int(sum([data[index - 1], data[index + 1]]))
                    data[index - 1] = int(sum([data[index - 1], data[index + 1]]))
                    forbidden_indexes.append(index)
                    forbidden_indexes.append(index + 1)
                    ok = True

        if forbidden_indexes == []:
            break

        data = [i for index, i in enumerate(data) if index not in forbidden_indexes]


    for index, i in enumerate(data, start=1):
        if isinstance(i, int):
            last_value = i
            if index == 1:
                ans = last_value
            if index < len(data):
                last_operator = data[index]
                if index + 1 < len(data):
                    if last_operator == '+':
                        ans += data[index + 1]
                    if last_operator == '-':
                        ans -= data[index + 1]
                    if last_operator == '*':
                        ans *= data[index + 1]
                    last_value = ans
    return ans


if __name__ == '__main__':
    symbols = ['+', '-', '*', '(', ')']
    with open('input.txt') as f:
        all_data = f.read().split('\n')
    total = []
    for data in all_data:
        while True:
            data = data.replace('(', ('\n(')).replace(')', ')\n').split('\n')
            for index, i in enumerate(data):
                if '(' in i and ')' in i:
                    eq = [int(i) if i not in symbols else i for i in i.replace('(', '', ).replace(')', '').split(' ')]
                    data[index] = str(solve_1(eq))
            data = ''.join(data)
            if '(' not in data:
                break

        data = [int(i) if i not in symbols else i for i in data.split(' ')]
        total.append(solve_1(data))
    # TO test part 1 remove the while loop in solve_1
    print('Part 2:', sum(total))
