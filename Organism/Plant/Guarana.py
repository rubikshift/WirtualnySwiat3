from World import WorldField as Species
from Organism.Plant import Plant


class Guarana(Plant):
    def __init__(self, worldToLive, position=None):
        super().__init__(0, worldToLive, position)
        self.Species = Species.GUARANA

    def __repr__(self):
        return "Guarana"

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Guarana(self.WorldToLive, childPosition)
            super().Reproduce()

    def Collide(self, anotherOrganism):
        anotherOrganism.Buff(3)
