if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
    all_allergens = set()
    d = {}
    for i in data:
        i = i.split('(contains ')
        ingredients, allergens = i[0].split(), i[1].strip(')').split(', ')
        for a in allergens:
            all_allergens.add(a)
            if d.get(a, None) is None:
                d[a] = {'possibilities': [],
                        'count': 0}
            d[a]['count'] += 1
            for ingredient in sorted(ingredients):
                d[a]['possibilities'].append(ingredient)


    def count_occurrences(l):
        f = {}
        for i in l:
            if f.get(i, None) is None:
                f[i] = 0
            f[i] += 1
        return f


    m = {}
    for k in sorted(d, key=lambda k: d[k]['count'], reverse=True):
        occs = count_occurrences(sorted(d[k]['possibilities']))
        to_delete = None

        for x, y in occs.items():
            if y >= d[k]['count'] and x not in m.values():
                m[k] = x
                break

    for k in sorted(d, key=lambda k: d[k]['count'], reverse=True):
        occs = count_occurrences(sorted(d[k]['possibilities']))
        to_delete = None

        for x, y in occs.items():
            if y >= d[k]['count'] and x not in m.values():
                # print(k, x, d[k]['count'])
                m[k] = x
                break

    leftovers = set()
    for k in d:
        for i in d[k]['possibilities']:
            leftovers.add(i)
    total = 0
    with open('input.txt') as f:
        data = f.read().split('\n')
    d = {}
    for i in data:
        i = i.split('(contains ')
        ingredients, allergens = i[0].split(), i[1].strip(')').split(', ')
        for ingredient in ingredients:
            if ingredient not in m.values():
                total += 1
    print('Part 1:', total)
    print('Part 2', ','.join([m[i] for i in sorted(m.keys())]))
