import math


def solve(data):
    answer = 0
    while True:
        result = math.floor(data / 3) - 2
        if result >= 0:
            answer += result
            data = result
        else:
            return answer


if __name__ == '__main__':
    answer = 0
    with open('input.txt') as f:
        for i in f.readlines():
            answer += solve(int(i))
    print(answer)
