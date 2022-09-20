from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget

from game.eight_puzzle import EightPuzzle
from ui import Gui


class Board(QWidget, Gui.Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.puzzle = None
        self.setupUi(self)
        self.btBlocks = [self.bt1, self.bt2, self.bt3, self.bt4, self.bt5, self.bt6, self.bt7, self.bt8, None]
        self.create_puzzle()
        self.connect_signals()

    def connect_signals(self):
        self.btrand.clicked.connect(self.randomize_handler)
        self.bt1.clicked.connect(lambda: self.block_click_handler(self.bt1))
        self.bt2.clicked.connect(lambda: self.block_click_handler(self.bt2))
        self.bt3.clicked.connect(lambda: self.block_click_handler(self.bt3))
        self.bt4.clicked.connect(lambda: self.block_click_handler(self.bt4))
        self.bt5.clicked.connect(lambda: self.block_click_handler(self.bt5))
        self.bt6.clicked.connect(lambda: self.block_click_handler(self.bt6))
        self.bt7.clicked.connect(lambda: self.block_click_handler(self.bt7))
        self.bt8.clicked.connect(lambda: self.block_click_handler(self.bt8))
        self.btsol.clicked.connect(self.solve_handler)

    def solve_handler(self):
        self.toggle_buttons()
        result, time = self.puzzle.a_star()
        path = self.puzzle.find_path(result)
        self.update_labels(len(path) - 1, round(time, 2))
        self.present_path(path, 0)

    def clear_labels(self):
        self.movesLab.setText('')
        self.timeLab.setText('')

    def update_labels(self, path_len, time):
        self.movesLab.setText("Finished with {0} Moves".format(path_len))
        self.timeLab.setText("In {0} Seconds".format(time))

    def present_path(self, path, i):
        if i == len(path):
            self.toggle_buttons()
            return
        self.set_board(path[i])
        QTimer.singleShot(1000, lambda: self.present_path(path, i + 1))

    def block_click_handler(self, button):
        block_number = int(button.text())
        position = self.puzzle.currentState.pattern.index(block_number)
        sx, sy = position // 3, position % 3
        destination = -1
        if sx < 2 and self.puzzle.currentState[(sx + 1) * 3 + sy] == 9:
            destination = (sx + 1) * 3 + sy
        elif sx > 0 and self.puzzle.currentState[(sx - 1) * 3 + sy] == 9:
            destination = (sx - 1) * 3 + sy
        elif sy < 2 and self.puzzle.currentState[sx * 3 + sy + 1] == 9:
            destination = sx * 3 + sy + 1
        elif sy > 0 and self.puzzle.currentState[sx * 3 + sy - 1] == 9:
            destination = sx * 3 + sy - 1
        if destination != -1:
            self.move_block(block_number, destination + 1)

    def create_puzzle(self):
        pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.puzzle = EightPuzzle(pattern)
        self.puzzle.shuffle_puzzle()
        self.set_board(self.puzzle.currentState.pattern)

    def randomize_handler(self):
        self.puzzle.shuffle_puzzle()
        self.clear_labels()
        self.set_board(self.puzzle.currentState.pattern)

    def toggle_buttons(self):
        enable = self.btsol.isEnabled()
        self.btsol.setEnabled(enable)
        self.btrand.setEnabled(enable)
        for bt in self.btBlocks:
            if bt:
                bt.setEnabled(enable)

    def move_block(self, block_number, destination):
        geometry_positions = {0: (10, 10), 1: (60, 10), 2: (110, 10),
                              3: (10, 60), 4: (60, 60), 5: (110, 60),
                              6: (10, 110), 7: (60, 110), 8: (110, 110)}
        position = self.puzzle.currentState.pattern.index(block_number)
        x, y = geometry_positions[destination - 1]
        w, h = self.btBlocks[block_number - 1].width(), self.btBlocks[block_number - 1].height()
        self.btBlocks[block_number - 1].setGeometry(QRect(x, y, w, h))
        self.puzzle.currentState.swap_blocks(position, destination - 1)

    def set_board(self, pattern):
        for i, p in enumerate(pattern):
            if p != 9:
                self.move_block(p, i + 1)
