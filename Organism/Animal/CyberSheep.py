from Organism.Animal import Animal
from World.WorldField import WorldField as Species


class CyberSheep(Animal):
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
            CyberSheep(self.WorldToLive, childPosition)
            self.WorldToLive.AddLog("Milosc rosnie wokol nas! Rodzi sie nowe zwierzatko (" + str(self) + ")")

    def Act(self):
        p = self.WorldToLive.FindClosestHogweed(self.Position)
        a, b = p
        x, y = self.Position
        futurePos = self.Position
        if a == -1 or b == -1:
            super().Act()
        else:
            self.WorldToLive.AddLog(str(self) + " namierzyla barszcz (" + str(a) + ", " + str(b) +
                                    "), wyznaczanie trasy z (" + str(x) + ", " + str(y) + ")")
            if a - x > 0:
                futurePos = x + 1, y
            elif a - x < 0:
                futurePos = x - 1, y
            elif b - y > 0:
                futurePos = x, y + 1
            elif b - y < 0:
                futurePos = x, y - 1

            anotherOrganism = self.WorldToLive.FindOrganism(futurePos)
            if anotherOrganism is not None:
                self.Collide(anotherOrganism)
                if anotherOrganism.IsDead is True:
                    self.Position = futurePos
            else:
                self.Position = futurePos
