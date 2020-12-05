if __name__ == '__main__':
    print(next(f'part 1 :{k}\npart 2 :{v}' for k, v in {max(data):next(i for i in range(min(data), max(data)) if i - 1 in data and i + 1 in data and i not in data) for data in [[int(x.translate({70: '0', 66: '1', 76: '0', 82: '1'}), 2) for x in open('input.txt').read().split('\n')]]}.items()))
