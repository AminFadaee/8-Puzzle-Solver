from PySide6.QtWidgets import QApplication

from GameBoard import Board
import sys
# This module runs the game.
app = QApplication(sys.argv)
board = Board()
board.show()
app.exec_()