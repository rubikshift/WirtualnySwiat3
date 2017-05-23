from Organism import Organism
from Organism.Plant import Plant


class Animal(Organism):
    def __init__(self, strength, initiative, worldToLive, position=0):
        super().__init__(strength, initiative, worldToLive, position)
        self.MoveDistance = 1

    def Act(self):
        return

    def Collide(self, anotherOrganism):
        if isinstance(anotherOrganism, Plant):
            self.Eat(anotherOrganism)
        elif anotherOrganism.DeflectedAttack(self) and not anotherOrganism.RunAway(self):
            self.Fight(anotherOrganism)
