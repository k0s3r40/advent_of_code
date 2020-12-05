if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
    trans ={70: '0', 66: '1', 76: '0', 82: '1'}
    data = [int(i.translate(trans), 2) for i in data]
    print(max(data), [i for i in range(min(data), max(data)) if i-1 in data and i+1 in data and i not in data][0])