from units.cell import Cell
from units.field import Field
from units.game_over import GameOver, Escaped
from units.terrain import Wall, Grass, Key, Door, Trap
from units.unit import Ghost


class GameController:
    def __init__(self, labyrinth):
        self.mapping = {'Wall': '🐍',
                        'Grass': '❎',
                        'Ghost': '👻',
                        'Key': '🔑',
                        'Door': '🗄️',
                        'Trap': '💀'
                        }
        self.game_on = True
        self.hero = Ghost()
        self.map_file = {'W': Wall(), 'g': Grass(), 'G': self.hero, 'K': Key(), 'D': Door(), 'T': Trap()}
        self.field = Field(unit=self.hero, field=self.fill_field(labyrinth))

    def fill_field(self, labyrinth):
        field = []
        for i in range(len(labyrinth)):
            field.append([])
            for j in range(len(labyrinth[i])):
                if labyrinth[i][j] == "G":
                    self.hero.coord = tuple((j,i))
                field[i].append(Cell(self.map_file[labyrinth[i][j]]))
        return field

    def print_field(self):
        for i in self.field.field:
            print(*[self.mapping[x.get_name()] for x in i], sep="")
        pass

    def play(self):
        while self.game_on and not self.hero.escaped:
            try:
                self.print_field()
                self.field.hero_move(move=input())
            except GameOver as e:
                print(e)
                self.game_on = False
            except Escaped as e:
                print(e)
                self.game_on = False
