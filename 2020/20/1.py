if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    d = {}
    for i in data:
        key = i.split('\n')[0]
        original = [x.replace('#', '1').replace('.', '0') for x in i.split('\n')[1:]]
        # original_reversed = [x[::-1] for x in original[1:]]
        rotated = [x[0] for x in list(zip(original[::-1]))]
        # rotated_reversed = [int(x[0], 2) for x in list(zip(original_reversed[::-1]))]
        original_values = [(int(original[0], 2), int(original[-1], 2)),
                           ((int(''.join([y[0] for y in original]), 2)), (int(''.join([y[-1] for y in original]), 2)))
                           ]
        rotated_values = [(int(rotated[0], 2), int(rotated[-1], 2)),
                          ((int(''.join([y[0] for y in rotated]), 2)), (int(''.join([y[-1] for y in rotated]), 2)))
                          ]
        # original_reversed = [int(x, 2) for x in original_reversed]
        d[key] = [original_values, rotated_values]
        # print(key, original,original_reversed, rotated, rotated_reversed)
    # 210..948
    for k, v in d.items():
        print(k)
        for i in v:
            print(i)
