class Tile:
    def __init__(self, tile, name):
        self.tile = tile
        self.neighbours_top = set()
        self.neighbours_bot = set()
        self.neighbours_left = set()
        self.neighbours_right = set()
        self.name = name

    def sides(self):
        return [self.top(), self.top()[::-1],
                self.bot(), self.bot()[::-1],
                self.right(), self.right()[::-1],
                self.left(), self.left()[::-1]
                ]

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
    for k, v in d.items():
        for y, x in d.items():
            if k != y:
                for side in v.sides():
                    for _ in x.sides():
                        if side == _:
                            a[k] += 1
    answer = 1
    for k, v in a.items():
        if v == 4:
            answer *= int(k.split(' ')[1][:-1])
    return answer



if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    d = {}
    for i in data:
        key = i.split('\n')[0]
        tile = [x for x in i.split('\n')[1:]]
        d[key] = Tile(tile, name=key)
    print(solve_1(d))