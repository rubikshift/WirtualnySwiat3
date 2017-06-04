from World.WorldField import WorldField as Species
from Organism.Plant import Plant


class SowThistle(Plant):
    def __init__(self, worldToLive, position=None, file=None):
        super().__init__(0, worldToLive, position, file)
        self.Species = Species.SOW_THISTLE

    def __repr__(self):
        return "Mlecz"

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            SowThistle(self.WorldToLive, childPosition)
            super().Reproduce()