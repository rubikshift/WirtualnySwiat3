from Organism.Plant import Plant
from World import WorldField as Species


class SosnowskyHogweed(Plant):
    def __init__(self, worldToLive, position=None):
        super().__init__(10, worldToLive, position)
        self.Species = Species.SOSNOWSKY_HOGWEED
        self.ReproduceProbability = 15

    def __repr__(self):
        return "Barsz Sosnowskiego"

    def Collide(self, anotherOrganism):
        anotherOrganism.Posion()

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = SosnowskyHogweed(self.WorldToLive, childPosition)
            super().Reproduce()

    def Act(self):
        x, y = self.Position

        left = x - 1, y
        right = x + 1, y
        up = x, y - 1
        down = x, y + 1

        self.WorldToLive.FindOrganism(left).Poison
        self.WorldToLive.FindOrganism(right).Poison()
        self.WorldToLive.FindOrganism(up).Poison()
        self.WorldToLive.FindOrganism(down).Poison()
