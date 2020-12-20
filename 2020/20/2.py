import numpy as np

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    d = {}
    for i in data:
        key = i.split('\n')[0]
        original = [x for x in i.split('\n')[1:]]
        rot_0 = np.array([list(i) for i in original])
        rot_1 = np.rot90(rot_0)
        rot_2 = np.rot90(rot_1)
        rot_3 = np.rot90(rot_2)

        original = [x for x in i.split('\n')[1:]][::-1]
        rot_0_f1 = np.array([list(i) for i in original])
        rot_1_f2 = np.rot90(rot_0)
        rot_2_f3 = np.rot90(rot_1)
        rot_3_f4 = np.rot90(rot_2)
        d[i] = {}
        d[key] = {'0': {'t': ''.join(rot_0[0]),
                        'b': ''.join(rot_0[-1]),
                        'l': ''.join([i[0] for i in rot_0]),
                        'r': ''.join([i[-1] for i in rot_0]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '1': {'t': ''.join(rot_1[0]),
                        'b': ''.join(rot_1[-1]),
                        'l': ''.join([i[0] for i in rot_1]),
                        'r': ''.join([i[-1] for i in rot_1]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '2': {'t': ''.join(rot_2[0]),
                        'b': ''.join(rot_2[-1]),
                        'l': ''.join([i[0] for i in rot_2]),
                        'r': ''.join([i[-1] for i in rot_2]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '3': {'t': ''.join(rot_3[0]),
                        'b': ''.join(rot_3[-1]),
                        'l': ''.join([i[0] for i in rot_3]),
                        'r': ''.join([i[-1] for i in rot_3]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '4': {'t': ''.join(rot_0_f1[0]),
                        'b': ''.join(rot_0_f1[-1]),
                        'l': ''.join([i[0] for i in rot_0_f1]),
                        'r': ''.join([i[-1] for i in rot_0_f1]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '5': {'t': ''.join(rot_1_f2[0]),
                        'b': ''.join(rot_1_f2[-1]),
                        'l': ''.join([i[0] for i in rot_1_f2]),
                        'r': ''.join([i[-1] for i in rot_1_f2]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '6': {'t': ''.join(rot_2_f3[0]),
                        'b': ''.join(rot_2_f3[-1]),
                        'l': ''.join([i[0] for i in rot_2_f3]),
                        'r': ''.join([i[-1] for i in rot_2_f3]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },
                  '7': {'t': ''.join(rot_3_f4[0]),
                        'b': ''.join(rot_3_f4[-1]),
                        'l': ''.join([i[0] for i in rot_3_f4]),
                        'r': ''.join([i[-1] for i in rot_3_f4]),
                        'occ_t': 0,
                        'occ_b': 0,
                        'occ_l': 0,
                        'occ_r': 0,
                        },

                  }
        tl = []
        for k in list(d):
            for sub_l in list(d[k]):
                t = d[k][sub_l]['t']
                b = d[k][sub_l]['b']
                l = d[k][sub_l]['l']
                r = d[k][sub_l]['r']
                for y in list(d):
                    for schema in d[y]:
                        is_top_valid = False
                        is_bot_valid = False
                        is_left_valid = False
                        is_right_valid = False
                        if t == d[y][schema]['b']:
                            is_top_valid = True
                            d[k][sub_l]['occ_t'] += 1
                        if b == d[y][schema]['t']:
                            is_bot_valid = True
                            d[k][sub_l]['occ_b'] += 1
                        if l == d[y][schema]['r']:
                            is_left_valid = True
                            d[k][sub_l]['occ_l'] += 1
                        if r == d[y][schema]['l']:
                            is_bot_valid = True
                            d[k][sub_l]['occ_r'] += 1
                        # if '3079' in k:
                        #     print(is_top_valid, is_bot_valid, is_left_valid, is_right_valid)
                        # if is_top_valid is False and is_bot_valid is True and is_left_valid is True and is_right_valid is False:
                        #     print('Top Right:', k, is_top_valid, is_bot_valid, is_left_valid,  is_right_valid)
                        #     input()

        for k in list(d):
            occs = 0
            for sub_l in list(d[k]):
                ff = d[k][sub_l]
                print(k, ff)
            print('----')
