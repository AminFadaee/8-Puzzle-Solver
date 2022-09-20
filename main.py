import sys

from PySide6.QtWidgets import QApplication

from game.game_board import Board

if __name__ == '__main__':
    app = QApplication(sys.argv)
    board = Board()
    board.show()
    app.exec_()
