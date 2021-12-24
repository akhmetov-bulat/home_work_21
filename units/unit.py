class Unit:
    def __init__(self, coord=(1, 1), hp=50):
        self.hp = hp
        self.coord = coord
        self.got_key = False
        self.escaped = False
        self.name = self.__class__.__name__.capitalize()

    def set_coord(self, x, y):
        self.coord = tuple((x, y))

    def get_coordinates(self):
        return self.coord

    def has_position(self, x, y):
        return (x, y) == self.coord

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        pass

    def is_alive(self):
        return self.hp > 0


class Ghost(Unit):

    def get_damage(self, damage):
        self.hp = self.hp - damage
