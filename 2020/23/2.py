if __name__ == '__main__':
    cups = [int(i) for i in '389125467']
    moves = 10
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

        destination_cup_index = leftover_cups.index(destination_cup)

        left_1 = leftover_cups[:destination_cup_index]
        left_2 = leftover_cups[destination_cup_index:][1:]

        leftover_cups = left_1 + [destination_cup] + picked_up + left_2 + [current_cup]

        cups = leftover_cups
    index_1 = cups.index(1)
    cups = cups[index_1:]+cups[index_1:][1:]
    print('part 1:', cups[1] + cups[0])
