from random import randint as rand


class Organism:

    Strength = None
    Initiative = None
    WorldToLive = None
    Age = None
    IsDead = None
    IsTurnedAllowed = None
    Position = None
    Species = None

    def __init__(self, strength, initiative, worldToLive, position=None):
        self.Strength = strength
        self.Initiative = initiative
        self.WorldToLive = worldToLive
        self.Age = 0
        self.IsDead = False
        self.IsTurnAllowed = False
        ok = False
        if position is not None:
            x, y = position
            self.Position = x, y
            ok = True
        while not ok:
            x = rand(0, worldToLive.Width)
            y = rand(0, worldToLive.Height)
            p = x, y
            o = worldToLive.FindOrganism(p)
            if o is None:
                ok = True
        self.Position = x, y
        self.WorldToLive.AddOrganism(self)

    def GetOlder(self):
        self.Age += 1

    def Draw(self):
        x, y = self.Position
        self.WorldToLive.Map[x][y] = self.Species

    def Fight(self, enemy):
        if self.Strength >= enemy.Strength:
            self.Kill(enemy)
        else:
            enemy.Kill(self)

    def DeflectedAttack(self, enemy):
        return False

    def RunAway(self, enemy):
        return False

    def Eat(self, somePlant):
        self.WorldToLive.AddLog(str(self) + " zjada " + str(somePlant))
        somePlant.Collide(self)
        somePlant.Die()

    def Buff(self, buffValue):
        self.Strength += buffValue
        self.WorldToLive.AddLog(str(self) + " staje sie silniejszy")

    def Die(self):
        self.IsDead = True

    def AllowMakingTurns(self):
        self.IsTurnAllowed = True

    def Kill(self, anotherOrganism):
        self.WorldToLive.AddLog(str(self) + " zabija " + str(anotherOrganism))
        anotherOrganism.Die()

    def Poison(self):
        self.IsDead = True

    def GetChildPosition(self):
        x, y = self.Position
        childPosition = self.Position
        left = x - 1, y
        right = x + 1, y
        up = x, y - 1
        down = x, y + 1

        oL = self.WorldToLive.FindOrganism(left)
        oR = self.WorldToLive.FindOrganism(right)
        oU = self.WorldToLive.FindOrganism(up)
        oD = self.WorldToLive.FindOrganism(down)

        ok = False
        while not ok:
            dir = rand(0, 3)

            if dir == 0 and x - 1 >= 0 and oL is None:
                childPosition = left
                ok = True
            elif dir == 1 and x + 1 < self.WorldToLive.Width and oR is None:
                childPosition = right
                ok = True
            elif dir == 2 and y - 1 >= 0 and oU is None:
                childPosition = up
                ok = True
            elif dir == 3 and y + 1 < self.WorldToLive.Height and oD is None:
                childPosition = down
                ok = True

        return childPosition

