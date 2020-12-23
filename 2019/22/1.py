class Deck:
    def __init__(self, deck_size):
        self.deck_size = deck_size
        self.my_deck = [i for i in range(self.deck_size)]

    def deal_to_new_deck(self):
        self.my_deck = self.my_deck[::-1]

    def cut_cards(self, n):
        if n < 0:
            n = self.deck_size - n
        self.my_deck = self.my_deck[n:] + self.my_deck[:n]

    def deal_with_increment(self, n):
        positions = ['-' for i in range(self.deck_size)]
        start = 0
        f = 0
        rotation = 0
        leftover = 0
        possible_positions = [i for i in range(self.deck_size) if i % n == 0]
        while '-' in positions:
            for index, value in enumerate(positions, start=0):
                if index in possible_positions:
                    if value == '-':
                        positions[index] = f
                        f += 1
                        last_index = index
            start_pos = 0
            while last_index < self.deck_size - 1:
                start_pos += 1
                last_index += 1

            start_pos = n - start_pos
            possible_positions = []
            i = start_pos - 1
            while i <= self.deck_size:
                possible_positions.append(i)
                i += n

        self.my_deck = positions

    def get_card_index(self, n):
        return self.my_deck[n - 1]

    def result(self):
        print(self.my_deck)


if __name__ == '__main__':
    with open('input.txt')as f:
        data = f.read().split('\n')
    my_deck = Deck(10)
    for i in data:
        i = i.split()
        if i[0] == 'cut':
            my_deck.cut_cards(int(i[-1]))
        elif i[0] == 'deal' and i[1] == 'with' and i[2] == 'increment':
            my_deck.deal_with_increment(int(i[-1]))
        elif i[0] == 'deal' and i[-1] == 'stack':
            my_deck.deal_to_new_deck()
    # 5667
    # print(my_deck.get_card_index(2019))
    my_deck.result()
