from Organism.Plant import Plant
from World.WorldField import WorldField as Species


class SosnowskyHogweed(Plant):
    def __init__(self, worldToLive, position=None, file=None):
        super().__init__(10, worldToLive, position, file)
        self.Species = Species.SOSNOWSKY_HOGWEED
        self.ReproduceProbability = 15

    def __repr__(self):
        return "Barszcz Sosnowskiego"

    def Collide(self, anotherOrganism):
        anotherOrganism.Poison()

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            SosnowskyHogweed(self.WorldToLive, childPosition)
            super().Reproduce()

    def Act(self):
        x, y = self.Position

        left = x - 1, y
        right = x + 1, y
        up = x, y - 1
        down = x, y + 1

        oL = self.WorldToLive.FindOrganism(left)
        oR = self.WorldToLive.FindOrganism(right)
        oU = self.WorldToLive.FindOrganism(up)
        oD = self.WorldToLive.FindOrganism(down)

        if oL is not None:
            oL.Poison()
        if oR is not None:
            oR.Poison()
        if oU is not None:
            oU.Poison()
        if oD is not None:
            oD.Poison()
