def get_dependencies(data, bag_type):
    dependencies = {k: [] for k in data.keys()}
    for k, value in data.items():
        for v in value:
            key = (' '.join(v.split()[1:]))
            if dependencies.get(key, None) is not None:
                dependencies[key].append(k)
    return dependencies[bag_type]


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i for i in f.read().split('\n') if 'contain no other bags' not in i]
    data = {i.split('contain')[0].strip().split('bag')[0].strip(): [x.strip().strip('.').split('bag')[0].strip() for x in i.split('contain')[1].split(',')] for
            i in data}

    deps = []
    my_bag = 'shiny gold'
    dependencies = get_dependencies(data, my_bag)

    deps += dependencies
    for i in dependencies:
        dependencies = get_dependencies(data, i)
        deps += dependencies
    for i in deps:
        dependencies = get_dependencies(data, i)
        deps += dependencies

    alternative = []
    answer_1 = 0
    alternatives = []
    for k, value in data.items():
        to_append = sum([int(v.split('shiny gold')[0].strip()) for v in value if 'shiny gold' in v])
        if to_append > 0:
            alternatives.append(k)
            answer_1 += 1
    answer_1 += len(alternatives)
    print('part 1:', answer_1)
