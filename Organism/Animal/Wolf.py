from World import WorldField as Species
from Organism.Animal import Animal


class Wolf(Animal):
    def __init__(self, worldToLive, position=None):
        super().__init__(9, 5, worldToLive, position)
        self.Species = Species.WOLF

    def __repr__(self):
        return "Wilk"

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Wolf):
            self.Reproduce()
        else:
            super().Collide()

    def Reproduce(self):
        childPosition = self.GetChildPostion()
        if childPosition != self.Position:
            young = Wolf(self.WorldToLive, childPosition)
            super().Reproduce()
