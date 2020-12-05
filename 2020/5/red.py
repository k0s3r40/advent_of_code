import math, itertools

def get_Row(ticket, col=None):
    if col:
        s_val = [0,7]
        r_index = (7, 10)
    else:
        s_val = [0, 127]
        r_index = (0, 7)

    for r_instr in range(r_index[0], r_index[1]):

        if ticket[r_instr] in ["B", "R"]:
            if r_instr == r_index[1] - 1:
                return s_val[1]
            else:
                s_val[0] = math.ceil(sum(s_val) / 2) #ceiling to round up for the upper calculation
        elif ticket[r_instr] in ["F", "L"]:
            if r_instr == r_index[1] - 1:
                return s_val[0]
            else:
                s_val[1] = (sum(s_val)) // 2 #Integer divide to round up for upper half calculation

b_passes = [x.strip() for x in open('input.txt').readlines()]
seat_ids = [(get_Row(ticket) * 8 + get_Row(ticket, True)) for ticket in b_passes]
print(min(seat_ids))
#Generates seats, but excludes those that I don't have boarding passes for
valid_seats = [x*8 + y for x,y in (itertools.product(range(math.ceil((min(seat_ids)-7)/8 + 1),(max(seat_ids)-7)//8), range(0, 8)))]
print(min(valid_seats), max(valid_seats))
print(set(valid_seats))
print(f'Part 1: The highest seat ID is {max(seat_ids)}')
print(f'Part 2: Your seat is {set(valid_seats) - set (seat_ids)}')