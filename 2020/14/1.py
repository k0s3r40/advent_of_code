import re


def solve(data):
    addresses = dict()
    mask = ''
    for i in data:
        if 'mask' in i:
            mask = i.replace('mask = ', '').strip()
        else:
            address, value = (int(re.findall(r'\d+', i.split()[0])[0]), "{0:b}".format(int(i.split()[2])))
            value = value.rjust(len(mask), '0')
            if addresses.get(address, None) is not None:
                addresses[address] = ''

            addresses[address] = [x for x in value]

            for i, v in enumerate(mask):
                if v != 'X':
                    addresses[address][i] = v
            addresses[address] = ''.join(addresses[address])

    print('Part 1:', sum([int(v, 2) for k, v in addresses.items()]))


def solve2(data):
    addresses = dict()
    mask = ''
    mask_x_count = 0
    storage = dict()
    for i in data:
        if 'mask' in i:
            mask = i.replace('mask = ', '').strip()
            mask_x_count = sum([1 for i in mask if i == 'X'])
        else:
            address, value, address_value, mem_addr = (int(re.findall(r'\d+', i.split()[0])[0]),
                                                       "{0:b}".format(int(i.split()[2])),
                                                       "{0:b}".format(int(re.findall(r'\d+', i.split()[0])[0])),
                                                       int(i.split()[2])
                                                       )

            value = value.rjust(len(mask), '0')
            address_value = address_value.rjust(len(mask), '0')
            if addresses.get(address, None) is not None:
                addresses[address] = ''

            combinations = ["{0:b}".format(int(i)).rjust(mask_x_count, '0') for i in range(2 ** mask_x_count)]

            addresses[address] = [x for x in address_value]

            for i, v in enumerate(addresses[address]):
                addresses[address][i] = mask[i] if mask[i] in ['X', '1'] else v

            addr_index = [i for i, n in enumerate(addresses[address]) if n == 'X']
            for comb in combinations:
                result = addresses[address]
                for x, value in enumerate(comb):
                    result[addr_index[x]] = value
                temp_add = int(''.join(result), 2)
                if storage.get(temp_add, None) is None:
                    storage[temp_add] = []
                storage[temp_add] = mem_addr
            addresses[address] = ''.join(addresses[address])

    print('Part 2:', sum([v for k, v in storage.items()]))


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
    solve(data)
    solve2(data)
