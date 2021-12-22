from units.field import Field
from units.game_over import GameOver, Escaped
from units.terrain import Wall, Grass, Key, Door, Trap
from units.unit import Ghost


class GameController:
    def __init__(self):
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
        self.gui_field = []
        self.field_file = "units/field.txt"
        self.field = Field(unit=self.hero, field_file=self.field_file, map_file=self.map_file)

    def print_field(self):
        for i in self.field.field:
            print(*[self.mapping[x.name] for x in i], sep="")
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
