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
    for rule in rules[0]:
        for index, r in enumerate(rule):
            if isinstance(r, str):
                regex += f'({r})'
            else:
                for i in r:
                    # print(flatten_list(i)[:-4])
                    regex += f'(({flatten_list(i)[:-4]})'

    # for i in range(10):
    #     regex = regex.replace("|)|()", ')').replace('|)','')

    # regex = regex.replace('()', '').replace('|)', ')').replace('))|(', '(')
    # regex =
    print(regex)
    #not 468
    # r = re.compile(regex, re.VERBOSE)
    # valid_messages = list(filter(r.match, messages)) # Read Note
    # print(len(valid_messages))
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
