from units.field import Field
from units.game_over import GameOver, Escaped
from units.terrain import Wall, Grass, Key, Door, Trap
from units.unit import Ghost


class GameController:
    def __init__(self):
        self.mapping = {'Wall': '🔲',
                        'Grass': '❎',
                        'Ghost': '👻',
                        'Key': '🗝',
                        'Door': '🚪',
                        'Trap': '💀'
                        }
        self.mapping_2= {'W': '🐍', 'g': '❎', 'G': '👻', 'K': '🔑', 'D': '🗄️', 'T': '💀'}
        self.game_on = True
        self.hero = None
        self.gui_field = []
        self.field = self.make_field()


    def make_field(self):
        field = []
        with open("field.txt", "r", encoding="utf-8") as f:
            i = 0
            for raw_row in f:
                row = raw_row.strip()
                field.append([])
                self.gui_field.append([])
                for j in range(len(row)):
                    field[i].append(self.init_cell(name=row[j], coord=(j, i)))
                    self.gui_field[i].append(self.mapping_2[row[j]])
                i += 1
        a=[]
        a.extend(self.gui_field)
        a[0][0] = "asdf"
        return Field(unit=self.hero, field=field, rows=len(field), cols=len(field[0]))


    def play(self):
        while self.game_on and not self.hero.escaped:
            self.field.print_field()
            try:
                self.field.hero_move(move=input())
            except GameOver as e:
                print(e)
                self.game_on = False
            except Escaped as e:
                print(e)
                self.game_on = False


    def init_cell(self, name, coord):
        if name == "W":
            return Wall()
        elif name == "g":
            return Grass()
        elif name == "G":
            self.hero = Ghost(coord=coord)
            return self.hero
        elif name == "K":
            return Key()
        elif name == "D":
            return Door()
        elif name == "T":
            return Trap()


game = GameController()
game.play()

