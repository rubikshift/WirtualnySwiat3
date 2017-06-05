from World.WorldField import WorldField
from math import inf, sqrt
from Organism import *


class World:
	Width = None
	Height = None
	Turn = None
	Organisms = None
	Map = None

	def __init__(self, width, height):
		self.Width = width
		self.Height = height
		self.Turn = 0
		self.Organisms = []
		self.Map = [[0 for x in range(width)] for y in range(height)]

	def MakeTurn(self):
		self.SortOrganisms()
		self.AllowMakingTurns()

		for o in self.Organisms:
			if o.IsDead is False and o.IsTurnAllowed is True:
				o.GetOlder()
				o.Act()
		self.Turn += 1
		return

	def Draw(self):
		for x in range(0, self.Width):
			for y in range(0, self.Height):
				self.Map[x][y] = WorldField.EMPTY

		for o in self.Organisms:
			if o.IsDead is False:
				o.Draw()
		return

	def Save(self):
		f = open("zapis.txt", "w", encoding="utf-8")
		f.write(str(self.Width) + '\n')
		f.write(str(self.Height) + '\n')
		f.write(str(self.Turn) + '\n')
		for o in self.Organisms:
			if o.IsDead is False:
				o.Save(f)
		f.close()
		return

	def Load(self):
		self.Organisms = []
		f = open("zapis.txt", "r", encoding="utf-8")
		self.Width = int(f.readline())
		self.Height = int(f.readline())
		self.Turn = int(f.readline())
		h = None
		while True:
			s = f.readline()
			if s == '':
				break
			elif s == "Owca\n":
				Sheep(self, file=f)
			elif s == "Antylopa\n":
				Antelope(self, file=f)
			elif s == "Cyber-owca\n":
				CyberSheep(self, file=f)
			elif s == "Lis\n":
				Fox(self, file=f)
			elif s == "Czlowiek\n":
				h = Human(self, file=f)
			elif s == "Zolw\n":
				Turtle(self, file=f)
			elif s == "Wilk\n":
				Wolf(self, file=f)
			elif s == "Wilcza jagoda\n":
				Belladona(self, file=f)
			elif s == "Guarana\n":
				Guarana(self, file=f)
			elif s == "Barszcz Sosnowskiego\n":
				SosnowskyHogweed(self, file=f)
			elif s == "Mlecz\n":
				SowThistle(self, file=f)
			elif s == "Trawa\n":
				Grass(self, file=f)
		f.close()
		return h

	def AddOrganism(self, livingOrganism):
		self.Organisms.append(livingOrganism)

	def SortOrganisms(self):
		self.Organisms = sorted(self.Organisms, key=lambda x: (x.Initiative, x.Age))

	def AllowMakingTurns(self):
		for x in self.Organisms:
			x.AllowMakingTurns()

	def AddLog(self, log):
		print(log)

	def FindOrganism(self, position):
		if self.CheckPoint(position) is False:
			return None
		for o in self.Organisms:
			if o.IsDead is False and o.Position == position:
				return o
		return None

	def FindClosestHogweed(self, position):
		x, y = position
		d = inf
		p = -1, -1
		for o in self.Organisms:
			if o.IsDead is False and isinstance(o, SosnowskyHogweed):
				a, b = o.Position
				tmp = sqrt((x - a) ** 2 + (y - b) ** 2)
				if tmp < d:
					d = tmp
					p = a, b
		return p

	def CheckPoint(self, point):
		x, y = point
		if x < 0 or x >= self.Width:
			return False
		if y < 0 or y >= self.Height:
			return False
		return True

	def IsEmptyNear(self, position):
		x, y = position

		left = x - 1, y
		right = x + 1, y
		up = x, y - 1
		down = x, y + 1

		oL = self.FindOrganism(left)
		oR = self.FindOrganism(right)
		oU = self.FindOrganism(up)
		oD = self.FindOrganism(down)

		if self.CheckPoint(left) and oL is None:
			return True
		elif self.CheckPoint(right) and oR is None:
			return True
		elif self.CheckPoint(up) and oU is None:
			return True
		elif self.CheckPoint(down) and oD is None:
			return True
		else:
			return False
