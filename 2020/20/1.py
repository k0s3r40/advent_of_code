class Tile:
    def __init__(self, tile, name):
        self.tile = tile
        self.neighbours_top = set()
        self.neighbours_bot = set()
        self.neighbours_left = set()
        self.neighbours_right = set()
        self.name = name
        self.is_corner = False

    def sides(self):
        return {"top": self.top(),
                "top_flipped": self.top()[::-1],
                "bot": self.bot(),
                "bot_flipped": self.bot()[::-1],
                "right": self.right(),
                "right_flipped": self.right()[::-1],
                "left": self.left(),
                "left_flipped": self.left()[::-1]
                }

    def sharps_count(self):
        return sum([1 if i == '#' else 0 for i in ''.join(self.tile)])

    def top(self):
        return ''.join(self.tile[0])

    def bot(self):
        return ''.join(self.tile[-1])

    def left(self):
        return ''.join([i[0] for i in self.tile])

    def right(self):
        return ''.join([i[-1] for i in self.tile])

    def flipX(self):
        self.tile = [i[::-1] for i in self.tile]

    def flipY(self):
        self.tile = [i for i in self.tile[::-1]]

    def rotate_90(self):
        new_tile = []
        self.flipX()
        for index, value in enumerate(self.tile):
            new_tile.append(''.join([i[index] for i in self.tile]))
        self.tile = new_tile

    def clear_neighbours(self):
        if len(self.neighbours_bot) >= 1:
            self.neighbours_bot = set()
        if len(self.neighbours_top) >= 1:
            self.neighbours_top = set()
        if len(self.neighbours_left) >= 1:
            self.neighbours_left = set()
        if len(self.neighbours_right) >= 1:
            self.neighbours_right = set()

    def neighbours_count(self):
        return sum([len(self.neighbours_left),
                    len(self.neighbours_right),
                    len(self.neighbours_top),
                    len(self.neighbours_bot)])


def find_neighbours(d):
    for k, v in d.items():
        for x, y in d.items():
            if k != x:
                if v.bot() == y.right():
                    v.rotate_90()
                    v.rotate_90()
                    v.rotate_90()

                if v.bot() == y.left():
                    v.rotate_90()
                    v.flipY()

                if v.top() == y.left():
                    v.rotate_90()
                    v.rotate_90()
                    v.rotate_90()

                if v.left() == y.left():
                    v.rotate_90()
                    v.rotate_90()
                    v.flipY()

                if v.top() == y.top():
                    v.flipX()

                if v.left() == y.right()[::-1]:
                    v.flipY()

                if v.right() == y.left()[::-1]:
                    v.flipY()

                if v.bot() == y.top():
                    v.neighbours_bot.add(y.name)

                if v.top() == y.bot():
                    v.neighbours_bot.add(y.name)

                if v.left() == y.right():
                    v.neighbours_left.add(y.name)

                if v.right() == y.left():
                    v.neighbours_right.add(y.name)

    return d


def solve_1(d):
    a = {k: 0 for k, v in d.items()}
    rel = {}
    for k, v in d.items():
        for y, x in d.items():
            if k != y:
                for side, side_v in v.sides().items():
                    for side_key, side_value in x.sides().items():
                        if side_v == side_value:
                            a[k] += 1
                            if rel.get((k, y), None) is None:
                                rel[(k, y)] = {}

                            rel[(k, y)][len(rel[(k, y)])] = {(side, side_key): (v, x)}


    answer = 1
    for k, v in a.items():
        if v == 4:
            answer *= int(k.split(' ')[1][:-1])
            for x, y in d.items():
                if y.name == k:
                    y.is_corner = True
    return answer


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    d = {}
    for i in data:
        key = i.split('\n')[0]
        tile = [x for x in i.split('\n')[1:]]
        d[key] = Tile(tile, name=key)

    print('Part 1:', solve_1(d))

    find_neighbours(d)
