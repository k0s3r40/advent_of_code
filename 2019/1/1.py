import math


def solve():
    with open('input.txt') as f:
        answer = sum([math.floor(int(i) / 3) - 2 for i in f.readlines()])
    return answer


if __name__ == '__main__':
    print(solve())
