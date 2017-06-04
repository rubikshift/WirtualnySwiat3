from World.WorldField import WorldField as Species
from Organism.Animal import Animal
from random import randint as rand


class Fox(Animal):
    def __init__(self, worldToLive, position=None, file=None):
        super().__init__(3, 7, worldToLive, position, file)
        self.Species = Species.FOX

    def __repr__(self):
        return "Lis"

    def Act(self):
        x, y = self.Position
        futurePos = self.Position
        left = x - 1, y
        right = x + 1, y
        up = x, y - 1
        down = x, y + 1

        oL = self.WorldToLive.FindOrganism(left)
        oR = self.WorldToLive.FindOrganism(right)
        oU = self.WorldToLive.FindOrganism(up)
        oD = self.WorldToLive.FindOrganism(down)

        if self.GoodNose() is False:
            self.WorldToLive.AddLog(str(self) + "nie zweszyl dobrego miejsca, tu mu dobrze")
            return
        self.WorldToLive.AddLog(str(self) + " zweszyl dobre miejsce")
        ok = False
        while not ok:
            dir = rand(0, 3)
            if dir == 0 and self.WorldToLive.IsProperPoint(left) and (oL is None or oL.Strength <= self.Strength):
                futurePos = left
                ok = True
            elif dir == 1 and self.WorldToLive.IsProperPoint(right) and (oR is None or oR.Strength <= self.Strength):
                futurePos = right
                ok = True
            elif dir == 2 and self.WorldToLive.IsProperPoint(up) and (oU is None or oU.Strength <= self.Strength):
                futurePos = up
                ok = True
            elif dir == 3 and self.WorldToLive.IsProperPoint(down) and (oD is None or oD.Strength <= self.Strength):
                futurePos = down
                ok = True
        anotherOrganism = self.WorldToLive.FindOrganism(futurePos)
        if anotherOrganism is not None:
            self.Collide(anotherOrganism)
            if anotherOrganism.IsDead:
                self.Position = futurePos
        else:
            self.Position = futurePos

    def GoodNose(self):
        x, y = self.Position
        left = x - 1, y
        right = x + 1, y
        up = x, y - 1
        down = x, y + 1

        oL = self.WorldToLive.FindOrganism(left)
        oR = self.WorldToLive.FindOrganism(right)
        oU = self.WorldToLive.FindOrganism(up)
        oD = self.WorldToLive.FindOrganism(down)

        if self.WorldToLive.IsProperPoint(left) and (oL is None or oL.Strength <= self.Strength):
            return True
        elif self.WorldToLive.IsProperPoint(right) and (oR is None or oR.Strength <= self.Strength):
            return True
        elif self.WorldToLive.IsProperPoint(up) and (oU in None or oU.Strength <= self.Strength):
            return True
        elif self.WorldToLive.IsProperPoint(down) and (oD in None or oD.Strength <= self.Strength):
            return True
        else:
            return False

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Fox):
            self.Reproduce()
        else:
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Fox(self.WorldToLive, childPosition)
            super().Reproduce()
