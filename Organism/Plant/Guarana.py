from World import WorldField as Species
from Organism.Plant import Plant


class Guarana(Plant):
    def __init__(self, worldToLive, position=0):
        super().__init__(0, worldToLive, position)
        self.Species = Species.GUARANA

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Guarana(self.WorldToLive, childPosition)

    def Collide(self, anotherOrganism):
        anotherOrganism.Buff(3)
