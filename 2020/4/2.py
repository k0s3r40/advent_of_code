import re


def get_height(hgt):
    if hgt is None:
        return False
    if hgt[-2:] == 'cm':
        return int(hgt[:-2]) in [i for i in range(150, 194)]
    if hgt[-2:] == 'in':
        return int(hgt[:-2]) in [i for i in range(59, 77)]
    return False


def solve(data):
    correct = 0
    regex = r'^#(?:[0-9a-fA-F]{6})$'
    regex_pid = r'^(?:[0-9a-fA-F]{9})$'

    for i in data:
        valid_ranges = {
            'byr': int(i.get('byr', 0)) in [i for i in range(1920, 2003)],
            'iyr': int(i.get('iyr', 0)) in [i for i in range(2010, 2021)],
            'eyr': int(i.get('eyr', 0)) in [i for i in range(2020, 2031)],

            'ecl': i.get('ecl', None) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],

            'hgt': get_height(i.get('hgt',None )),
            'hcl': re.search(regex, i.get('hcl', '0')) is not None,
            'pid': re.search(regex_pid, i.get('pid', '0')) is not None,
        }
        if all(valid_ranges.values()):
            correct +=1
    return correct


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()

    data = data.split('\n\n')
    d = []
    for x in data:
        d.append({i.split(":")[0]: i.split(':')[1] for i in x.split()})
    print(solve(d))
    #
    # keywords = [
    #     'byr',
    #     'iyr',
    #     'eyr',
    #     'hgt',
    #     'hcl',
    #     'ecl',
    #     'pid',
    #     # 'cid',
    # ]
    # print(solve(keywords, data))
