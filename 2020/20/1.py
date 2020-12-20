if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    d = {}
    for i in data:
        key = i.split('\n')[0]
        original = [x for x in i.split('\n')[1:]]
        original_reversed = [x[::-1] for x in original]
        rotated = [x[0] for x in list(zip(original[::-1]))]
        rotated_reversed = [x[0] for x in list(zip(original_reversed))]
        # print(original)
        # print(original_reversed)
        print(len(original), len(original_reversed), len(rotated_reversed), len(rotated))
        original_values = [((original[0]),
                            (original[-1])),
                           (((''.join([y[0] for y in original]))),
                            ((''.join([y[-1] for y in original]))))
                           ]
        original_reversed_values = [((original_reversed[0]),
                                     (original_reversed[-1])),
                                    (((''.join([y[0] for y in original_reversed]))),
                                     ((''.join([y[-1] for y in original_reversed]))))
                                    ]
        rotated_values = [((rotated[0]),
                           (rotated[-1])),
                          (((''.join([y[0] for y in rotated]))),
                           ((''.join([y[-1] for y in rotated]))))
                          ]
        rotated_reversed_values = [((rotated_reversed[0]),
                                    (rotated_reversed[-1])),
                                   (((''.join([y[0] for y in rotated_reversed]))),
                                    ((''.join([y[-1] for y in rotated_reversed]))))
                                   ]

        d[key] = {'0': {'t': original_values[0][1],
                        'b': original_values[0][0],
                        'l': original_values[1][0],
                        'r': original_values[1][1],
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '1': {'t': original_reversed_values[0][0],
                        'b': original_reversed_values[0][1],
                        'l': original_reversed_values[1][0],
                        'r': original_reversed_values[1][1],
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '2': {'t': rotated_values[1][1],
                        'b': rotated_values[1][0],
                        'l': rotated_values[0][0],
                        'r': rotated_values[0][1],
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '3': {'t': rotated_reversed_values[0][0],
                        'b': rotated_reversed_values[0][1],
                        'l': rotated_reversed_values[1][0][::-1],
                        'r': rotated_reversed_values[1][1][::-1],
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        }
                  }
    # angle one occurence top bot and one occurence left right

    for k in list(d):
        for sub_l in list(d[k]):
            t = d[k][sub_l]['t']
            b = d[k][sub_l]['b']
            l = d[k][sub_l]['l']
            r = d[k][sub_l]['r']
            for y in list(d):
                for i in d[y]:
                    if t == d[y][i]['b']:
                        d[y][i]['occ_t'] += 1
                        d[k][sub_l]['occ_t'] += 1
                    if b == d[y][i]['t']:
                        d[y][i]['occ_b'] += 1
                        d[k][sub_l]['occ_b'] += 1
                    if l == d[y][i]['r']:
                        d[y][i]['occ_l'] += 1
                        d[k][sub_l]['occ_l'] += 1
                    if r == d[y][i]['l']:
                        d[y][i]['occ_r'] += 1
                        d[k][sub_l]['occ_r'] += 1

    for k in list(d):
        for sub_l in list(d[k]):
            print(k, d[k][sub_l])
        print('----')
