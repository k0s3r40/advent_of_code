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


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
    solve(data)
