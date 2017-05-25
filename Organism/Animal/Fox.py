from World import WorldField as Species
from Organism.Animal import Animal


class Fox(Animal):
    def __init__(self, worldToLive, position=0):
        super().__init__(3, 7, worldToLive, position)
        self.Species = Species.FOX

    def Act(self):
        return

    def GoodNose(self):
        return

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Fox):
            self.Reproduce()
        else:
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Fox(self.WorldToLive, childPosition)
