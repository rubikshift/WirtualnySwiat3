from random import randint as rand


class Organism:
    def __init__(self, strength, initiative, worldToLive, position=0):
        self.Strength = strength
        self.Initiative = initiative
        self.WorldToLive = worldToLive
        self.Age = 0
        self.IsDead = False
        self.IsTurnAllowed = False
        ok = False
        if position != 0:
            x, y = position
            self.Position = x, y
            ok = True
        while not ok:
            x = rand(0, worldToLive.Width)
            y = rand(0, worldToLive.Height)
            #Sprawdzic czy zajete
            ok = True
        self.Position = x, y

    def GetOlder(self):
        self.Age += 1

    def Draw(self):
        x, y = self.Position
        self.WorldToLive.Map[x][y] = self.Species

    def Fight(self, enemy):
        #dodac logi
        if self.Strength >= enemy.Strength:
            self.Kill(enemy)
        else:
            enemy.Kill(self)

    def DeflectedAttack(self, enemy):
        return False

    def RunAway(self, enemy):
        return False

    def Eat(self, somePlant):
        #dodac logi
        somePlant.Collide(self)
        somePlant.Die()

    def Buff(self, buffValue):
        self.Strength += buffValue
        #dodac logi

    def Die(self):
        self.IsDead = True

    def AllowMakingTurns(self):
        self.IsTurnAllowed = True

    def Kill(self, anotherOrganism):
        anotherOrganism.Die()