from World import WorldField as Species
from Organism.Plant import Plant


class Grass(Plant):
    def __init__(self, worldToLive, position=0):
        super().__init__(0, worldToLive, position)
        self.Species = Species.GRASS

    def Act(self):
        for i in range(0, 3):
            super().Act()

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Grass(self.WorldToLive, childPosition)
