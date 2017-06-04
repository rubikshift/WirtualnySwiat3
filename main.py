import sys
from PyQt5.QtWidgets import *
from World import *
from Organism import *


if __name__ == '__main__':

    w = World(10, 10)
    for i in range(4):
        Sheep(w)
        Turtle(w)
        Wolf(w)
        SosnowskyHogweed(w)
    CyberSheep(w)
    CyberSheep(w)
    while True:
        w.MakeTurn()
