if __name__ == '__main__':
    cups = [int(i) for i in '123487596']
    moves = 100
    step = 3
    for i in range(moves):
        current_cup = cups[0]
        picked_up = cups[1:4]
        leftover_cups = cups[4:]

        destination_cup = current_cup - 1
        while destination_cup not in leftover_cups:
            destination_cup -= 1
            if destination_cup < min(cups):
                destination_cup = max(leftover_cups)
                break
        left_1 = []
        left_2 = []
        for i in leftover_cups:
            if i != destination_cup:
                left_1.append(i)
            else:
                break
        for i in leftover_cups:
            if i not in left_1:
                left_2.append(i)
        left_2 = left_2[1:]

        leftover_cups = left_1 + [destination_cup] + picked_up + left_2 + [current_cup]

        cups = leftover_cups
    cups = ''.join([str(i) for i in cups]).split('1')
    print('part 1:', cups[1] + cups[0])
