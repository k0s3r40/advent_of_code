class Player:
    def __init__(self, deck, player_name):
        self.deck = deck
        self.player_name = player_name
        self.deck_states = []

    def get_top_card(self):
        if len(self.deck) > 0:
            return self.deck[0]
        else:
            return False

    def append_cards(self, my_card, the_other_card, is_main_game = True):
        if is_main_game is True:
            for i in sorted([my_card, the_other_card], reverse=True):
                self.deck.append(i)
        else:
            self.deck.append(my_card)
            self.deck.append(the_other_card)

    def remove_top_card(self):
        self.deck_states.append(deck)
        self.deck = self.deck[1:]


    def print_deck(self):
        print(self.deck)

def recursive_fight(deck_1, deck_2):
    player_1 = Player(deck_1, 'p1')
    player_2 = Player(deck_2, 'p2')
    round = 1
    winner = ''
    while True:
        p1_card = player_1.get_top_card()
        p2_card = player_2.get_top_card()
        if p1_card and p2_card:
            player_1.remove_top_card()
            player_2.remove_top_card()
            if p1_card <= len(player_1.deck) and p2_card <= len(player_2.deck):

                rec_winner = recursive_fight(player_1.deck, player_2.deck)
                if rec_winner == 'p1':
                    player_1.append_cards(p1_card, p2_card, is_main_game=False)
                else:
                    player_2.append_cards(p2_card, p1_card, is_main_game=False)
            else:
                if p1_card > p2_card:
                    player_1.append_cards(p1_card, p2_card)
                else:
                    player_2.append_cards(p2_card, p1_card)
            round += 1
        else:
            if p1_card:
                winner = 'p1'
            else:
                winner = 'p2'
            break
    return winner

if __name__ == '__main__':
    with open('input.txt')as f:
        data = f.read().split('\n\n')

    player_1 = None
    player_2 = None

    for player_data in data:
        player_data = player_data.split('\n')
        player_name = player_data[0]
        deck = [int(i) for i in player_data[1:]]
        if player_1 is None:
            player_1 = Player(deck, player_name)
        else:
            player_2 = Player(deck, player_name)

    round = 1

    while True:
        p1_card = player_1.get_top_card()
        p2_card = player_2.get_top_card()
        if p1_card and p2_card:
            player_1.remove_top_card()
            player_2.remove_top_card()
            if p1_card <= len(player_1.deck) and p2_card <= len(player_2.deck):

                rec_winner = recursive_fight(player_1.deck, player_2.deck)
                if rec_winner == 'p1':
                    player_1.append_cards(p1_card, p2_card, is_main_game=False)
                else:
                    player_2.append_cards(p2_card, p1_card, is_main_game=False)
            else:
                if p1_card > p2_card:
                    player_1.append_cards(p1_card, p2_card)
                else:
                    player_2.append_cards(p2_card, p1_card)
            round += 1
        else:
            break


    deck = []
    if player_1.get_top_card():
        deck = player_1.deck
    else:
        deck = player_2.deck

    x = len(deck)

    answer = 0

    for i in deck:
        answer += (i * x)
        x -= 1

    print('Part 1:', answer)
