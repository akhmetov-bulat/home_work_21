class Unit:
    def __init__(self):
        self.hp = 0
        self.got_key = False
        self.coord = (0, 0)
        self.escaped = False

    def __repr__(self):
        return "Unit"

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        pass

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp = self.hp - damage

    def set_coordinates(self, x, y):
        self.coord = (x, y)

    def get_coordinates(self):
        return self.coord

    def has_position(self, x, y):
        return (x, y) == self.coord


class Ghost(Unit):
    def __init__(self, coord=(1,1), hp=50):
        super().__init__()
        self.name = "Ghost"
        self.hp = hp
        self.coord = coord

    def __repr__(self):
        return '👻'
