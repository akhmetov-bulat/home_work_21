from units.game_over import GameOver, Escaped
from units.unit import Unit


class Terrain:
    def __init__(self, terrain, is_walkable):
        self.is_walkable = is_walkable
        self.terrain = terrain

    def __repr__(self):
        return "Terrain"

    def is_walkable(self):
        return self.is_walkable()

    def terrain(self):
        return self.terrain()

    def step_on(self, unit: Unit):
        return True


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain="door", is_walkable=False)

    def __repr__(self):
        return '🗄️'

    def step_on(self, unit: Unit):
        if unit.has_key:
            self.is_walkable = True
            raise Escaped("You escaped")
        return False


class Key(Terrain):
    def __init__(self):
        super().__init__(terrain="key", is_walkable=True)

    def __repr__(self):
        return '🔑'

    def step_on(self, unit: Unit):
        unit.got_key = True
        return True


class Trap(Terrain):
    def __init__(self, damage=30):
        super().__init__(terrain="Trap", is_walkable=True)
        self.damage = damage

    def __repr__(self):
        return '💀'

    def step_on(self, unit: Unit):
        if self.damage >= unit.hp:
            unit.hp = 0
            raise GameOver("Game Over")
        else:
            unit.hp -= self.damage
        return True


class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain="grass", is_walkable=True)

    def __repr__(self):
        return '❎'


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain="wall", is_walkable=False)

    def __repr__(self):
        return '🐍'

    def step_on(self, unit: Unit):
        return False
