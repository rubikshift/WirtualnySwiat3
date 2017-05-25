from World import WorldField as Species
from Organism.Animal import Animal
from random import randint as rand

class Turtle(Animal):
    def __init__(self, worldToLive, position=0):
        super().__init__(2, 1, worldToLive, position)
        self.Species = Species.TURTLE

    def DeflectedAttack(self, enemy):
        if enemy.Strength < 5:
            return True
        else:
            return False

    def Act(self):
        i = rand(1, 100)
        if i > 75:
            super().Act()

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Turtle):
            self.Reproduce()
        else:
            super().Collide(anotherOrganism)

    def Reproduce(self):
        childPosition = self.GetChildPosition()
        if childPosition != self.Position:
            young = Turtle(self.WorldToLive, childPosition)
