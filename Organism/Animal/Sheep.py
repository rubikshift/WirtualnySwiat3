from World import WorldField as Species
from Organism.Animal import Animal


class Sheep(Animal):
    def __init__(self, worldToLive, position=None):
        super().__init__(4, 4, worldToLive, position)
        self.Species = Species.SHEEP

    def __repr__(self):
        return "Owca"

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Sheep):
            self.Reproduce()
        else:
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Sheep(self.WorldToLive, childPosition)
            super().Reproduce()
