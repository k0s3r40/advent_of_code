def solve(data):
    valid = 0
    for i in data:
        if i['range'][0] <= i['password'].count(i['letter']) <= i['range'][1]:
            valid += 1

    return valid

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [{"range":[int(x) for x in i.split(':')[0].split(' ')[0].split('-')],
                 "letter":i.split(':')[0].split(' ')[1],
                 "password":i.split(':')[1].strip()
                 } for i in f.readlines()]
    print(solve(data))
