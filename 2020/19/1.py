import operator
from functools import reduce
from itertools import chain
import re


def check_sub(rules):
    for rule in rules[0]:
        for condition in rule:
            if isinstance(rules[condition], str):
                return rules[condition]
            else:
                check_sub(rules[condition])


def flatten_list(l, s=''):
    for i in l:
        try:
            s += f'{"".join(i)})|('
        except:
            s = flatten_list(i, s)
    return f'{s}'


def solve(rules, messages):
    regex = ''
    rule = rules[0]
    # print(rules[0][0])

    regex = r"""
       a((aa|bb)(ab|ba))|((ab|ba)(aa|bb))b
    """
    regex = str(rules[0]).replace(
        '[', '('
    ).replace(
        ']', ')'
    ).replace(
        ', ', ''
    ).replace(
        '\'', ''
    ).replace('))((', ')(')
    print(regex)
    # regex = regex[1:-1]
    # re_elements_to_replace = re.findall(r'\w+\)\(\w+', regex)
    # for i in re_elements_to_replace:
    #     regex = regex.replace(i, i.replace(')(', '|'))
    # re_elements_to_replace = re.findall(r'\(\(\w+', regex)
    # for i in re_elements_to_replace:
    #     regex = regex.replace(i, i.replace('((', '('))
    # print('a((aa|bb)(ab|ba))|((ab|ba)(aa|bb))b')
    # print(regex)

    # regex = regex.replace(')|(', '|')
    # for i in range(10):
    #     regex = regex.replace("|)|()", ')').replace('|)','')

    # regex = regex.replace('()', '').replace('|)', ')').replace('))|(', '(')
    # regex =

    # print(regex)
    # not 468, 416, 469

    r = re.compile(regex, re.VERBOSE)
    valid_messages = list(filter(r.match, messages))

    print(len(valid_messages))


if __name__ == '__main__':
    with open('input.txt') as f:
        data, messages = f.read().split('\n\n')
        data = data.split('\n')
        messages = messages.split('\n')
    d = {}

    for i in data:
        rule_id = int(i.split(':')[0])
        conditions = i.split(':')[1].split('|')
        d[rule_id] = []
        for c in conditions:
            if '\"' in c:
                c = c.replace('\"', '').strip()
                d[rule_id] = c
            else:
                c = [int(y) for y in (c.split())]
                d[rule_id].append(c)

    to_replace = {}
    for i in list(d):
        to_replace[i] = d[i]

    for i in list(d):
        if not isinstance(d[i], str):
            for index, condition in enumerate(d[i]):
                d[i][index] = [str(x) if x not in to_replace.keys() else to_replace[x] for x in d[i][index]]

    solve(d, messages)
