from Organism.Animal import Animal
from Organism.Plant import Plant
from World import WorldField as Species
from random import randint as rand


class Antelope(Animal):
    def __init__(self, worldToLive, position=None):
        super().__init__(4, 4, worldToLive, position)
        self.MoveDistance = 2
        self.Species = Species.ANTELOPE

    def __repr__(self):
        return "Antylopa"

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Antelope):
            self.Reproduce()
        elif isinstance(anotherOrganism, Plant) or not self.RunAway(anotherOrganism):
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Antelope(self.WorldToLive, childPosition)
            super().Reproduce()

    def RunAway(self):
        i = rand(1, 100)
        if i <= 50 and self.WorldToLive.IsEmptyNear(self.Position):
            self.Position = self.GetChildPosition()
            self.WorldToLive.AddLog(str(self) + " uciekla")
            return True
        else:
            return False
