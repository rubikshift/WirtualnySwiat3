from Organism import Organism
from Organism.Plant import Plant
from random import randint as rand


class Animal(Organism):

    MoveDistance = None

    def __init__(self, strength, initiative, worldToLive, position=None):
        super().__init__(strength, initiative, worldToLive, position)
        self.MoveDistance = 1

    def Act(self):
        x, y = self.Position
        futurePos = self.Position
        left = x - 1, y
        right = x + 1, y
        up = x, y - 1
        down = x, y + 1

        ok = False
        while not ok:
            dir = rand(0, 3)
            if dir == 0 and x - 1 >= 0:
                futurePos = left
            elif dir == 1 and x + 1 < self.WorldToLive.Width:
                futurePos = right
            elif dir == 2 and y - 1 >= 0:
                futurePos = up
            elif dir == 3 and y + 1 < self.WorldToLive.Heigth:
                futurePos = down

            if self.Position != futurePos:
                ok = True

        anotherOrganism = self.WorldToLive.FindOrganism(futurePos)
        if anotherOrganism is not None:
            self.Collide(anotherOrganism)
            if anotherOrganism.IsDead is True:
                self.Position = futurePos
        else:
            self.Position = futurePos

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Plant):
            self.Eat(anotherOrganism)
        elif not anotherOrganism.DeflectedAttack(self) and not anotherOrganism.RunAway(self):
            self.Fight(anotherOrganism)

    def Reproduce(self):
        self.WorldToLive.AddLog("Milosc rosnie wokol nas! Rodzi sie nowe zwierzatko (" + str(self) + ")")
