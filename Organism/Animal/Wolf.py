from World.WorldField import WorldField as Species
from Organism.Animal import Animal


class Wolf(Animal):
    def __init__(self, worldToLive, position=None, file=None):
        super().__init__(9, 5, worldToLive, position, file)
        self.Species = Species.WOLF

    def __repr__(self):
        return "Wilk"

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Wolf):
            self.Reproduce()
        else:
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            Wolf(self.WorldToLive, childPosition)
            super().Reproduce()
