from World.WorldField import WorldField as Field


class World:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        self.Turn = 0

    def MakeTurn(self):
        return

    def Draw(self):
        for x in range(0, self.Width):
            for y in range(0, self.Height):
                self.Map[x][y] = Field.EMPTY
        return

    def Save(self):
        return

    def Load(self):
        return
