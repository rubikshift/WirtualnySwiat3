from World.WorldField import WorldField as Species
from Organism.Plant import Plant


class Grass(Plant):
    def __init__(self, worldToLive, position=None, file=None):
        super().__init__(0, worldToLive, position, file)
        self.Species = Species.GRASS

    def __repr__(self):
        return "Trawa"

    def Act(self):
        for i in range(0, 3):
            super().Act()

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            Grass(self.WorldToLive, childPosition)
            super().Reproduce()
