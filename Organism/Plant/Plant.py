from Organism import Organism
from random import randint as rand


class Plant(Organism):
    def __init__(self, strength, worldToLive, position=None):
        super().__init__(strength, 0, worldToLive, position)
        self.ReproduceProbability = 35

    def Act(self):
        p = rand(1, 100)
        if p <= self.ReproduceProbability:
            self.Reproduce()

    def Reproduce(self):
        self.WorldToLive.AddLog(str(self) + " rozsiewa sie")

    def Poison(self):
        return
