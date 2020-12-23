import re


def solve(regex, messages):
    r = re.compile(regex, re.VERBOSE)
    valid_messages = list(filter(r.match, messages))

    print(len(valid_messages))


if __name__ == '__main__':
    with open('input.txt') as f:
        data, messages = f.read().split('\n\n')
        data = data.split('\n')
        messages = messages.split('\n')
    a =  [f"8: {'|'.join([''.join(['42 '*(i+1)]) for i in range(50)])} ",
             f"11: {'| '.join([''.join(['42 '*(i+1)+ '31 '*(i+1)]) for i in range(50)])}"
             ]
    # for i in a:
    #     print(i)
    #     print('---------')
    # input()
    d = {}

    special = []
    for i in data:
        rule_id = int(i.split(':')[0])
        conditions = i.split(':')[1].split('|')
        d[rule_id] = ''
        for c in conditions:
            if '\"' in c:
                c = c.replace('\"', '').strip()
                d[rule_id] = c
                special.append(str(rule_id))
            else:

                c = str([int(y) for y in (c.split())]).replace(']', ')').replace('[', '(').replace(',', '')
                d[rule_id] += str(c)
    has_looped = False
    while True:
        d_temp = {**d}

        for i in sorted(list(d)):
            for s in special:
                d[i] = d[i].replace(f'({s} ', f'({d[int(s)]} ')
                d[i] = d[i].replace(f' {s})', f' {d[int(s)]})')
                d[i] = d[i].replace(f'({s})', f'({d[int(s)]})')
                d[i] = d[i].replace(f' {s} ', f' {d[int(s)]} ')

                is_special = True

                for x in d[i].replace('(', '').replace(')', ' ').replace('[', '').replace(']', '').replace('|', '').split():
                    try:
                        if x not in ['(', ')', ',', ' ', 'a', 'b', '\b', '+', '|']:
                            isinstance(int(i), int)
                            is_special = False

                    except Exception as E:
                        pass
                if is_special:
                    special.append(str(i))
                    special = list(set(special))
        if not re.findall('\d', str(d[0])):
            break
        if d_temp == d:
            has_looped = True

        # for k, v in d.items():
        #     print(k, v)

    regex = d[0].replace('))((', '))|((').replace(')(', '|').replace(' ', '')
    regex = f'^{regex}$'
    # print(regex)
    # Not 243
    # part 2 not 389, 301
    # 226
    solve(regex, messages)
