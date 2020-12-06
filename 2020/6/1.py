def solve_part_2(data):
    answers = 0
    for group in data:
        chunks = [set(sorted(chunk)) for chunk in group.splitlines()]
        answers += len(set.intersection(*map(set, chunks)))
    return answers

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    print('task 1:', sum(len(set(group.replace('\n', ''))) for group in data))
    solve_part_2(data)
    print('task 2:', solve_part_2(data))
