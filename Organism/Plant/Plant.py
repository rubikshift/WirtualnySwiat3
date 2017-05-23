from Organism import Organism
from random import randint as rand


class Plant(Organism):
    def __init__(self, strength, worldToLive, position=0):
        super().__init__(strength, 0, worldToLive, position)
        self.ReproduceProbability = 35

    def Act(self):
        p = rand(1, 100)
        if p <= self.ReproduceProbability:
            self.Reproduce()
