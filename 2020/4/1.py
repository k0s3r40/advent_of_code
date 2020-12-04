
def solve(keywords, data):
    correct = 0
    for i in data:
        is_correct = True
        for keyword in keywords:
            if keyword not in i:
                is_correct = False
        if is_correct:
            correct += 1
    return correct

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()

    data = data.split('\n\n')
    keywords = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid',
    ]
    print(solve(keywords, data))
