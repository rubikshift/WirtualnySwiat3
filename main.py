import sys
from PyQt5.QtWidgets import *
from World import *
from Organism import *


if __name__ == '__main__':

    w = World(10, 10)
    w.Load()
    while True:
        w.MakeTurn()
