from Organism.Animal import Animal
from World.WorldField import WorldField as Species


class Human(Animal):
	futurePos = None
	SuperPowerActive = None
	SuperPowerCoolDown = None
	SuperPowerTurnsLeft = None

	def __init__(self, worldToLive, position=None, file=None):
		super().__init__(5, 4, worldToLive, position, file)
		self.Species = Species.HUMAN
		if file is not None:
			self.SuperPowerCoolDown = int(file.readline())
			self.SuperPowerActive = bool(file.readline())
			self.SuperPowerTurnsLeft = int(file.readline())
		else:
			self.SuperPowerActive = False
			self.SuperPowerCoolDown = 0
			self.SuperPowerTurnsLeft = 0
			self.futurePos = None

	def __repr__(self):
		return "Czlowiek"

	def SuperPower(self):
		if self.SuperPowerActive is True or self.SuperPowerCoolDown > 0:
			return False
		else:
			self.WorldToLive.AddLog(str(self) + " uzywa mocy specjalnej")
			self.SuperPowerActive = True
			self.SuperPowerTurnsLeft = 5
			self.Strength += 5
			return True

	def Act(self):
		anotherOrganism = None
		if self.futurePos is not None:
			anotherOrganism = self.WorldToLive.FindOrganism(self.futurePos)
		if anotherOrganism is not None:
			self.Collide(anotherOrganism)
			if anotherOrganism.IsDead is True:
				self.Position = self.futurePos
		elif self.futurePos is not None:
			self.Position = self.futurePos

		if self.SuperPowerActive is False and self.SuperPowerCoolDown > 0:
			self.SuperPowerCoolDown -= 1
		elif self.SuperPowerActive is True:
			self.SuperPowerTurnsLeft -= 1
			self.Strength -= 1

		if self.SuperPowerActive is True and self.SuperPowerTurnsLeft == 0:
			self.WorldToLive.AddLog("Moc specjalna przestala dzialac")
			self.SuperPowerActive = False
			self.SuperPowerCoolDown = 5

	def Control(self, direction):
		return

	def Save(self, file):
		super().Save(file)
		file.write(str(self.SuperPowerCoolDown) + '\n')
		file.write(str(self.SuperPowerActive) + '\n')
		file.write(str(self.SuperPowerTurnsLeft) + '\n')
