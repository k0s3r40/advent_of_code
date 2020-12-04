import re


def get_height(hgt):
    if hgt is None:
        return False
    if hgt[-2:] == 'cm':
        return int(hgt[:-2]) in [i for i in range(150, 194)]
    if hgt[-2:] == 'in':
        return int(hgt[:-2]) in [i for i in range(59, 77)]
    return False


def solve(data, required_keys):
    correct_2 = 0
    correct_1 = 0
    regex = r'^#(?:[0-9a-fA-F]{6})$'
    regex_pid = r'^(?:[0-9a-fA-F]{9})$'

    for i in data:
        valid_ranges = {
            'byr': int(i.get('byr', 0)) in [i for i in range(1920, 2003)],
            'iyr': int(i.get('iyr', 0)) in [i for i in range(2010, 2021)],
            'eyr': int(i.get('eyr', 0)) in [i for i in range(2020, 2031)],
            'ecl': i.get('ecl', None) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            'hgt': get_height(i.get('hgt', None)),
            'hcl': re.search(regex, i.get('hcl', '0')) is not None,
            'pid': re.search(regex_pid, i.get('pid', '0')) is not None,
        }
        if all(valid_ranges.values()):
            correct_2 += 1
        is_correct_1 = True
        for key in required_keys:
            if key not in list(i):
                is_correct_1 = False
        if is_correct_1:
            correct_1+=1
    return  correct_1, correct_2


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    d = []
    for x in data.split('\n\n'):
        d.append({i.split(":")[0]: i.split(':')[1] for i in x.split()})
    required_keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',

    ]
    print(solve(d, required_keys))
