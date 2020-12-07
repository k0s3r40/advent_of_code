def get_containing(bag, data):
    try:
        return data[bag]
    except:
        return []


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [i for i in f.read().split('\n') if 'contain no other bags' not in i]
    data = {i.split('contain')[0].strip().split('bag')[0].strip(): [x.strip().strip('.').split('bag')[0].strip() for x in i.split('contain')[1].split(',')] for
            i in data}

    my_bag = 'shiny gold'
    dependencies = get_containing(my_bag, data)


    for i in dependencies:
        name = ' '.join(i.split(' ')[1:])
        qty = int(i.split(' ')[0])
        for i in range(qty):
            dependencies += get_containing(name, data)

    print('part2:',sum([int(i.split(' ')[0]) for i in dependencies]))

