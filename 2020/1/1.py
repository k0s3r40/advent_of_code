with open('input.txt') as f:
    data = [int(i) for i in f.readlines()]


def solve():
    for i in data:
        if 2020 - i in data:
            return i * (2020 - i)


if __name__ == '__main__':
    print(solve())
