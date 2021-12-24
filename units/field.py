from units.cell import Cell
from units.game_over import GameOver
from units.terrain import Grass, Wall, Key, Door, Trap
from units.unit import Ghost


class Field:
    def __init__(self, unit: Ghost, field):
        self.unit = unit
        self.field = field
        self.rows = len(self.field)
        self.cols = len(self.field[0])

    def hero_move(self, move):
        if move.casefold() == 'w':
            return self.move_unit_up()
        elif move.casefold() == 'a':
            return self.move_unit_left()
        elif move.casefold() == 's':
            return self.move_unit_down()
        elif move.casefold() == 'd':
            return self.move_unit_right()
        elif move.casefold() == "stop" or move.casefold() == "exit":
            raise GameOver("You exit game")

    def move_unit_up(self):
        x, y = self.unit.coord
        if y > 0 and self.field[y-1][x].get_obj().step_on(self.unit):
            self.unit.coord = tuple((x, (y - 1)))
            self.field[y - 1][x] = Cell(self.unit)
            self.field[y][x] = Cell(Grass())

    def move_unit_down(self):
        x, y = self.unit.coord
        if y < (self.rows-1) and self.field[y+1][x].get_obj().step_on(self.unit):
            self.unit.coord = tuple((x, (y + 1)))
            self.field[y + 1][x] = Cell(self.unit)
            self.field[y][x] = Cell(Grass())

    def move_unit_right(self):
        x, y = self.unit.coord
        if x < (self.cols - 1) and self.field[y][x+1].get_obj().step_on(self.unit):
            print(x, y)
            self.unit.coord = tuple(((x + 1), y))
            self.field[y][x + 1] = Cell(self.unit)
            self.field[y][x] = Cell(Grass())

    def move_unit_left(self):
        x, y = self.unit.coord
        if x > 0 and self.field[y][x - 1].get_obj().step_on(self.unit):
            self.unit.coord = tuple(((x - 1), y))
            self.field[y][x - 1] = Cell(self.unit)
            self.field[y][x] = Cell(Grass())
