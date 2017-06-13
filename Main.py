from GameBoard import Board
from PyQt4.QtGui import *
import sys
# This module runs the game.
app = QApplication(sys.argv)
board = Board()
board.show()
app.exec_()