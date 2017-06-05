import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QInputDialog, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from World import *
from Organism import *


class Game(QWidget):
	W = None
	H = None
	Ok = False

	def __init__(self):
		super().__init__()
		width, ok = QInputDialog.getInt(self,"Szerokosc swiata","wprowadz szerokosc", 20, 0, 42, 1)
		height, ok = QInputDialog.getInt(self,"wysokosc swiata","wprowadz wysokosc", 20, 0, 32, 1)

		self.W = World(width, height)
		self.H = Human(self.W)
		self.setFocusPolicy(Qt.StrongFocus)
		self.Start()
		self.Label = QLabel()
		saveButton = QPushButton("Zapisz")
		saveButton.clicked.connect(self.W.Save)
		loadButton = QPushButton("Wczytaj")
		loadButton.clicked.connect(self.Load)
		superButton = QPushButton("Super moc")
		superButton.clicked.connect(self.H.SuperPower)

		hbox = QHBoxLayout()
		hbox.addWidget(saveButton)
		hbox.addWidget(loadButton)
		hbox.addWidget(superButton)
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.Label)
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		vbox.addLayout(hbox2)

		self.setLayout(vbox)
		self.resize(1280, 960)
		self.center()
		self.setWindowTitle('Michal Krakowiak 165596')
		self.show()

	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

	def keyPressEvent(self, event):
		key = event.key()
		self.Ok = True
		if key == Qt.Key_Left:
			self.H.Control(0)
			self.W.MakeTurn()
		elif key == Qt.Key_Right:
			self.H.Control(1)
			self.W.MakeTurn()
		elif key == Qt.Key_Up:
			self.H.Control(2)
			self.W.MakeTurn()
		elif key == Qt.Key_Down:
			self.H.Control(3)
			self.W.MakeTurn()
		self.repaint()

	def mousePressEvent(self, event):
		p = event.pos()
		x = p.x()
		y = p.y()
		x = x // 30
		y = y // 30
		if self.W.CheckPoint((x,y)) and self.W.Map[x][y] == WorldField.EMPTY:
			items = ("Antylopa", "CyberOwca", "Lis", "Owca", "Zolw", "Wilk", "WilczaJagoda", "Trawa",
					"Guarana", "BarszczSosnowskiego", "Mlecz")
			item, ok = QInputDialog.getItem(self, "Stworz organizm", "wybierz organizm", items, 0, False)
			self.ParseTextToOrganism(item, (x, y))


	def paintEvent(self, e):
		self.W.Draw()
		self.UpdateLabel()
		qp = QPainter()
		qp.begin(self)
		self.Clear(qp)
		self.DrawOrganisms(qp)
		qp.end()

	def Clear(self, qp):
		for y in range(self.W.Height):
			for x in range(self.W.Width):
				qp.eraseRect(x*30, y*30, 30, 30)

	def DrawOrganisms(self, qp):
		col = QColor(0, 0, 0)
		col.setNamedColor('#d4d4d4')
		qp.setPen(col)
		for y in range(self.W.Height):
			for x in range(self.W.Width):
				qp.setBrush(self.ParseSpeciesToColor(self.W.Map[x][y]))
				qp.drawRect(x*30, y*30, 30, 30)

	def UpdateLabel(self):
		self.Label.setText("Sila czlowieka: " + str(self.H.Strength) + "; Do ponwnego uzycia mocy: " + str(self.H.SuperPowerCoolDown) +
							"; Czas trwania mocy: " + str(self.H.SuperPowerTurnsLeft))

	def ParseSpeciesToColor(self, species):
		if species == WorldField.ANTELOPE:
			return QColor(Qt.cyan)
		elif species == WorldField.SOW_THISTLE:
			return QColor(Qt.yellow)
		elif species == WorldField.SOSNOWSKY_HOGWEED:
			return QColor(Qt.red)
		elif species == WorldField.TURTLE:
			return QColor(Qt.blue)
		elif species == WorldField.GUARANA:
			return QColor(Qt.magenta)
		elif species == WorldField.SHEEP:
			return QColor(Qt.gray)
		elif species == WorldField.HUMAN:
			return QColor(Qt.black)
		elif species == WorldField.GRASS:
			return QColor(Qt.green)
		elif species == WorldField.BELLADONA:
			return QColor(Qt.darkBlue)
		elif species == WorldField.WOLF:
			return QColor(Qt.darkGray)
		elif species == WorldField.FOX:
			return QColor(255, 153, 0)		# orange
		elif species == WorldField.CYBER_SHEEP:
			return QColor(Qt.darkRed)
		else:
			return QColor(Qt.white)

	def ParseTextToOrganism(self, text, point):
		if text == "Owca":
			Sheep(self.W, position=point)
		elif text == "Antylopa":
			Antelope(self.W, position=point)
		elif text == "CyberOwca":
			CyberSheep(self.W, position=point)
		elif text == "Lis":
			Fox(self.W, position=point)
		elif text == "Zolw":
			Turtle(self.W, position=point)
		elif text == "Wilk":
			Wolf(self.W, position=point)
		elif text == "WilczaJagoda":
			Belladona(self.W, position=point)
		elif text == "Trawa":
			Grass(self.W, position=point)
		elif text == "Guarana":
			Guarana(self.W, position=point)
		elif text == "BarszczSosnowskiego":
			SosnowskyHogweed(self.W, position=point)
		elif text == "Mlecz":
			SowThistle(self.W, position=point)

	def Start(self):
		for i in range(4):
			Sheep(self.W)
			Wolf(self.W)
			Antelope(self.W)
			Turtle(self.W)
			Fox(self.W)
			Grass(self.W)
			SowThistle(self.W)
			SosnowskyHogweed(self.W)
			Belladona(self.W)
			Guarana(self.W)
			CyberSheep(self.W)

	def Load(self):
		self.H = self.W.Load()
		self.repaint()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	t = Game()
	sys.exit(app.exec_())
