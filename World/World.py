from World import WorldField


class World:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        self.Turn = 0
        self.Organisms = []
        self.Map = [[0 for x in range(width)] for y in range(height)]

    def MakeTurn(self):
        self.SortOrganisms()
        self.AllowMakingTurns()
        return

    def Draw(self):
        for x in range(0, self.Width):
            for y in range(0, self.Height):
                self.Map[x][y] = WorldField.EMPTY

        for o in self.Organisms:
            o.Act()
        return

    def Save(self):
        return

    def Load(self):
        return

    def AddOrganism(self, livingOrganism):
        self.Organisms.append(livingOrganism)

    def SortOrganisms(self):
        self.Organisms = sorted(self.Organisms, key=lambda x: (x.Initiative, x.Age))

    def AllowMakingTurns(self):
        for x in self.Organisms:
            x.AllowMakingTurns()

    def AddLog(self, log):
        print(log)

    def FindOrganism(self, position):
        for o in self.Organisms:
            if o.Position == position:
                return o
        return None
