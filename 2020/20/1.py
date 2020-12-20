
if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    d = {}
    for i in data:
        key = i.split('\n')[0]
        original = [x.replace('#','1').replace('.', '0') for x in i.split('\n')[1:]]
        original_reversed = [x[::-1] for x in original[1:]]
        rotated = [int(x[0], 2) for x in list(zip(original[::-1]))]
        rotated_reversed = [int(x[0], 2) for x in list(zip(original_reversed[::-1]))]
        original = [int(x,2) for x in original]
        original_reversed = [int(x, 2) for x in original_reversed]
        d[key] = [original_reversed,  rotated]
        # print(key, original,original_reversed, rotated, rotated_reversed)
    # 210..948
    for k ,v in d.items():
        print(k)
        for i in v:
            print(i)