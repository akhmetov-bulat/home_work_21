from units.game_controller import GameController



# def make_field(field_file,
#                map_file):
def read_labyrinth(labyrinth_file):
    field = []
    with open(labyrinth_file, "r", encoding="utf-8") as f:
        i = 0
        field_xy_list = [x.strip() for x in f.readlines()]
        return field_xy_list

    #

    # def init_cell(self, name, coord):
    #     if name == "W":
    #         return Wall()
    #     elif name == "g":
    #         return Grass()
    #     elif name == "G":
    #         self.unit.coord = coord
    #         return self.unit
    #     elif name == "K":
    #         return Key()
    #     elif name == "D":
    #         return Door()
    #     elif name == "T":
    #         return Trap()


labyrinth = read_labyrinth(labyrinth_file="units/field.txt")
game = GameController(labyrinth)
game.play()
