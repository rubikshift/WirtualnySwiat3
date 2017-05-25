from World import WorldField as Species
from Organism.Animal import Animal


class Sheep(Animal):
    def __init__(self, worldToLive, position=0):
        super().__init__(4, 4, worldToLive, position)
        self.Species = Species.SHEEP

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Sheep):
            self.Reproduce()
        else:
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Sheep(self.WorldToLive, childPosition)
