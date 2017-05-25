from World.WorldField import Species


class World:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        self.Turn = 0

    def MakeTurn(self):
        self.SortOrganisms()
        self.AllowMakingTurns()
        return

    def Draw(self):
        for x in range(0, self.Width):
            for y in range(0, self.Height):
                self.Map[x][y] = Species.EMPTY
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
