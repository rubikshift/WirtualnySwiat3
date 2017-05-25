from World import WorldField as Species
from Organism.Plant import Plant


class SowThistle(Plant):
    def __init__(self, worldToLive, position=0):
        super().__init__(0, worldToLive, position)
        self.Species = Species.SOW_THISTLE

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = SowThistle(self.WorldToLive, childPosition)