with open('input.txt') as f:
    data = [int(i) for i in f.readlines()]


def solve():
    for i in data:
        rest = 2020 - i
        for x in data:
            if i != x and x <= rest:
                if rest - x in data:
                    return i * x * (rest - x)
                else:
                    continue


if __name__ == '__main__':
    print(solve())
