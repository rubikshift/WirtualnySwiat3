from Organism.Animal.Sheep import Sheep
from World import WorldField as Species


class CyberSheep(Sheep):
    def __init__(self, worldToLive, position=None):
        super().__init__(11, 4, worldToLive, position)
        self.Species = Species.CYBER_SHEEP

    def __repr__(self):
        return "Cyber-owca"

    def Poison(self):
        return

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, CyberSheep):
            self.Reproduce()
        else:
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = CyberSheep(self.WorldToLive, childPosition)
            self.WorldToLive.AddLog("Milosc rosnie wokol nas! Rodzi sie nowe zwierzatko (" + str(self) + ")")

    def Act(self):
        return
