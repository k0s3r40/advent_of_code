def solve_1(data):
    ans = 0

    for index, i in enumerate(data, start=1):
        if isinstance(i, int):
            last_value = i
            if index == 1:
                ans = last_value
            if index < len(data):
                last_operator = data[index]
                if index + 1 < len(data):
                    if last_operator == '+':
                        ans += data[index + 1]
                    if last_operator == '-':
                        ans -= data[index + 1]
                    if last_operator == '*':
                        ans *= data[index + 1]
                    last_value = ans
    print(ans)


if __name__ == '__main__':
    symbols = ['+', '-', '*', '(', ')']
    with open('input.txt') as f:
        data = f.read()
    # print(data)
    # solve_1(data)
