from random import randint as rand


class Organism:
	Strength = None
	Initiative = None
	WorldToLive = None
	Age = None
	IsDead = None
	IsTurnAllowed = None
	Position = None
	Species = None

	def __init__(self, strength, initiative, worldToLive, position=None, file=None):
		self.IsDead = False
		self.IsTurnAllowed = False
		self.WorldToLive = worldToLive
		self.Initiative = initiative

		if file is not None:
			self.Position = eval(file.readline())
			self.Strength = int(file.readline())
			self.Age = int(file.readline())
		else:
			self.Strength = strength
			self.Age = 0
			ok = False
			if position is not None:
				x, y = position
				self.Position = x, y
				ok = True
			while not ok:
				x = rand(0, worldToLive.Width - 1)
				y = rand(0, worldToLive.Height - 1)
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

	def RunAway(self):
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

		if self.WorldToLive.IsEmptyNear(self.Position) is False:
			return childPosition

		ok = False
		while not ok:
			dir = rand(0, 3)

			if dir == 0 and self.WorldToLive.CheckPoint(left) and oL is None:
				childPosition = left
				ok = True
			elif dir == 1 and self.WorldToLive.CheckPoint(right) and oR is None:
				childPosition = right
				ok = True
			elif dir == 2 and self.WorldToLive.CheckPoint(up) and oU is None:
				childPosition = up
				ok = True
			elif dir == 3 and self.WorldToLive.CheckPoint(down) and oD is None:
				childPosition = down
				ok = True
		return childPosition

	def Save(self, file):
		file.write(str(self) + '\n')
		file.write(str(self.Position) + '\n')
		file.write(str(self.Strength) + '\n')
		file.write(str(self.Age) + '\n')

