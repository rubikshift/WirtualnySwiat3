from World import WorldField as Species
from Organism.Animal import Animal


class Wolf(Animal):
    def __init__(self, worldToLive, position=0):
        super().__init__(9, 5, worldToLive, position)
        self.Species = Species.WOLF

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Wolf):
            self.Reproduce()
        else:
            super().Collide()

    def Reproduce(self):
        childPosition = self.GetChildPostion()
        if childPosition != self.Position:
            young = Wolf(self.WorldToLive, childPosition)
