import sys
from PyQt5.QtWidgets import *
from World import *
from Organism import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    w = World(10, 10)
    h = Human(w)
    a = Antelope(w)
    b = Belladona(w)
    window.resize(600, 600)
    window.move(300, 300)
    window.setWindowTitle('Michal Krakowiak 165596')
    window.show()

    sys.exit(app.exec_())
