from units.game_over import GameOver
from units.terrain import Grass, Wall, Key, Door, Trap
from units.unit import Ghost


class Field:
    def __init__(self, unit: Ghost, field_file, map_file):
        self.unit = unit
        self.field = self.__make_field(field_file=field_file, map_file=map_file)
        self.rows = len(self.field)
        self.cols = len(self.field[0])


    def __make_field(self, field_file, map_file):
        field = []
        with open(field_file, "r", encoding="utf-8") as f:
            i = 0
            for raw_row in f:
                row = raw_row.strip()
                field.append([])
                for j in range(len(row)):
                    field[i].append(map_file[row[j]])
                    if row[j] == "G":
                        self.unit.set_coord(j, i)
                i += 1
        return field

    def init_cell(self, name, coord):
        if name == "W":
            return Wall()
        elif name == "g":
            return Grass()
        elif name == "G":
            self.unit.coord = coord
            return self.unit
        elif name == "K":
            return Key()
        elif name == "D":
            return Door()
        elif name == "T":
            return Trap()

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
            self.unit.coord = tuple((x, (y - 1)))
            self.field[y - 1][x] = self.unit
            self.field[y][x] = Grass()

    def move_unit_down(self):
        x, y = self.unit.coord
        if y < (self.rows-1) and self.field[y+1][x].step_on(self.unit):
            self.unit.coord = tuple((x, (y + 1)))
            self.field[y + 1][x] = self.unit
            self.field[y][x] = Grass()


    def move_unit_right(self):
        x, y = self.unit.coord
        if x < (self.cols - 1) and self.field[y][x+1].step_on(self.unit):
            print(x, y)
            self.unit.coord = tuple(((x + 1), y))
            self.field[y][x + 1] = self.unit
            self.field[y][x] = Grass()

    def move_unit_left(self):
        x, y = self.unit.coord
        if x > 0 and self.field[y][x - 1].step_on(self.unit):
            self.unit.coord = tuple(((x - 1), y))
            self.field[y][x - 1] = self.unit
            self.field[y][x] = Grass()
