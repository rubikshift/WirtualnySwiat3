from Organism import Organism
from Organism.Plant import Plant
from random import randint as rand


class Animal(Organism):

    MoveDistance = None

    def __init__(self, strength, initiative, worldToLive, position=None, file=None):
        super().__init__(strength, initiative, worldToLive, position, file)
        self.MoveDistance = 1

    def Act(self):
        x, y = self.Position
        futurePos = self.Position
        left = x - self.MoveDistance, y
        right = x + self.MoveDistance, y
        up = x, y - self.MoveDistance
        down = x, y + self.MoveDistance

        ok = False
        while not ok:
            dir = rand(0, 3)
            if dir == 0 and self.WorldToLive.CheckPoint(left):
                futurePos = left
            elif dir == 1 and self.WorldToLive.CheckPoint(right):
                futurePos = right
            elif dir == 2 and self.WorldToLive.CheckPoint(up):
                futurePos = up
            elif dir == 3 and self.WorldToLive.CheckPoint(down):
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
        elif not anotherOrganism.DeflectedAttack(self) and not anotherOrganism.RunAway():
            self.Fight(anotherOrganism)

    def Reproduce(self):
        self.WorldToLive.AddLog("Milosc rosnie wokol nas! Rodzi sie nowe zwierzatko (" + str(self) + ")")
