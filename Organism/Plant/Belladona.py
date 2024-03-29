from Organism.Plant import Plant
from World.WorldField import WorldField as Species


class Belladona(Plant):
    def __init__(self, worldToLive, position=None, file=None):
        super().__init__(99, worldToLive, position, file)
        self.ReproduceProbability = 15
        self.Species = Species.BELLADONA

    def __repr__(self):
        return "Wilcza jagoda"

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            Belladona(self.WorldToLive, childPosition)
            super().Reproduce()

    def Collide(self, anotherOrganism):
        self.Kill(anotherOrganism)


