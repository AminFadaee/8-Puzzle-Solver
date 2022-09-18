import sys

from PySide6.QtWidgets import QApplication

from game_board import Board

app = QApplication(sys.argv)
board = Board()
board.show()
app.exec_()
