from units.game_over import GameOver, Escaped
from units.unit import Unit, Ghost


class Terrain:
    def __init__(self):
        self.name = self.__class__.__name__.capitalize()

    def is_walkable(self):
        return self.is_walkable

    def terrain(self):
        return self.name

    def step_on(self, unit: Unit):
        return True


class Door(Terrain):
    def __init__(self):
        super().__init__()

    def step_on(self, unit: Ghost):
        if unit.has_key():
            raise Escaped("You escaped")
        return False


class Key(Terrain):
    def __init__(self):
        super().__init__()

    def step_on(self, unit: Ghost):
        unit.set_key()
        return True


class Trap(Terrain):
    def __init__(self, damage=30):
        super().__init__()
        self.damage = damage

    def step_on(self, unit: Ghost):
        if self.damage >= unit.hp:
            unit.hp = 0
            raise GameOver("Game Over")
        else:
            unit.hp -= self.damage
        return True


class Grass(Terrain):
    def __init__(self):
        super().__init__()


class Wall(Terrain):
    def __init__(self):
        super().__init__()

    def step_on(self, unit: Ghost):
        return False
