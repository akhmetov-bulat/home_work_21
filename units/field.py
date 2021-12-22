from units.game_over import GameOver
from units.terrain import Grass
from units.unit import Unit, Ghost


class Field:
    def __init__(self, unit, field, cols=0, rows=0):
        self.field = field
        self.cols = cols
        self.rows = rows
        self.unit = unit

    def cell(self, x, y):
        pass

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
        if y > 0 and self.field[y-1][x].step_on(self.unit):
            # self.field[y - 1][x].step_on(self.unit)
            self.unit.coord = tuple((x, (y - 1)))
            self.field[y - 1][x] = self.unit
            self.field[y][x] = Grass()

    def move_unit_down(self):
        x, y = self.unit.coord
        if y < (self.rows-1) and self.field[y+1][x].step_on(self.unit):
            # self.field[y + 1][x].step_on(self.unit)
            self.unit.coord = tuple((x, (y + 1)))
            self.field[y + 1][x] = self.unit
            self.field[y][x] = Grass()


    def move_unit_right(self):
        print("right")
        x, y = self.unit.coord
        if x < (self.cols - 1) and self.field[y][x+1].step_on(self.unit):
            # self.field[y][x + 1].step_on(self.unit)
            self.unit.coord = tuple(((x + 1), y))
            self.field[y][x + 1] = self.unit
            self.field[y][x] = Grass()

    def move_unit_left(self):
        x, y = self.unit.coord
        if x > 0 and self.field[y][x - 1].step_on(self.unit):
            # self.field[y][x - 1].step_on(self.unit)
            self.unit.coord = tuple(((x - 1), y))
            self.field[y][x - 1] = self.unit
            self.field[y][x] = Grass()


    def get_cols(self, x, y):
        return self.cols
        pass

    def get_rows(self, x, y):
        return self.rows
        pass

    def print_field(self):
        for i in self.field:
            print(*i, sep="")
        pass
