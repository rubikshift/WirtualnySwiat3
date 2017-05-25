from Organism.Plant import Plant
from World import WorldField as Species


class Belladona(Plant):
    def __init__(self, worldToLive, position=0):
        super().__init__(99, worldToLive, position)
        self.ReproduceProbability = 15
        self.Species = Species.BELLADONA

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Belladona(self.WorldToLive, childPosition)

    def Collide(self, anotherOrganism):
        self.Kill(anotherOrganism)


