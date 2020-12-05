if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n')
    data = [int(i.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for i in data]
    print(max(data), [i for i in range(min(data), max(data)) if i-1 in data and i+1 in data and i not in data][0])