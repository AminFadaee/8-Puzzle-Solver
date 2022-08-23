from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget

from ui import Gui
from EightPuzzle import EightPuzzle


class Board(QWidget, Gui.Ui_Form):
    # This class implements the user interface using PyQt4.
    # Variables:    btBlocks
    #               puzzle
    # Methods:      connectSignals
    #               solveHandler
    #               presentPath
    #               blockClickHandler
    #               createPuzzle
    #               randomizeHandler
    #               toggleButtons
    #               moveBlock
    #               setTheBoard
    def __init__(self):
        # The board contains 8 buttons for the blocks and each of them
        # (bti) are stored in btBlocks for ease of access. The other 2
        # buttons are btRand and btSol. There are two labels movesLab
        # and timeLab At the bottom of the window for status.First the
        # puzzle is created and stored in puzzle variable and then the
        # signals are connected for the buttons.
        QWidget.__init__(self)
        self.setupUi(self)
        self.btBlocks = [self.bt1, self.bt2, self.bt3, self.bt4, self.bt5, self.bt6, self.bt7, self.bt8, None]
        self.createPuzzle()
        self.connectSignals()

    def connectSignals(self):
        '''Connects the signals to the proper slots(handlers).'''
        self.btrand.clicked.connect(self.randomizeHandler)
        self.bt1.clicked.connect(lambda: self.blockClickHandler(self.bt1))
        self.bt2.clicked.connect(lambda: self.blockClickHandler(self.bt2))
        self.bt3.clicked.connect(lambda: self.blockClickHandler(self.bt3))
        self.bt4.clicked.connect(lambda: self.blockClickHandler(self.bt4))
        self.bt5.clicked.connect(lambda: self.blockClickHandler(self.bt5))
        self.bt6.clicked.connect(lambda: self.blockClickHandler(self.bt6))
        self.bt7.clicked.connect(lambda: self.blockClickHandler(self.bt7))
        self.bt8.clicked.connect(lambda: self.blockClickHandler(self.bt8))
        self.btsol.clicked.connect(self.solveHandler)

    def solveHandler(self):
        '''btSol handler'''
        # When the Solve button (btSol) is clicked the toggleButtons
        # is called to disable all of the buttons. The buttons are
        # Enabled later in presentPath method. The puzzle will be
        # solved using AStar and the status labels are updated. in
        # the end the path steps are shown on the board.
        self.toggleButtons()
        result, time = self.puzzle.AStar()
        path = self.puzzle.findPath(result)
        self.updateLabels(len(path) - 1, round(time, 2))
        self.presentPath(path, 0)

    def clear_labels(self):
        self.movesLab.setText('')
        self.timeLab.setText('')

    def updateLabels(self, pathLen, time):
        '''Updates the status labels'''
        self.movesLab.setText("Finished with {0} Moves".format(pathLen))
        self.timeLab.setText("In {0} Seconds".format(time))

    def presentPath(self, path, i):
        '''Shows the path steps on the board'''
        if i == len(path):
            self.toggleButtons()
            return
        self.setTheBoard(path[i])
        QTimer.singleShot(1000, lambda: self.presentPath(path, i + 1))

    def blockClickHandler(self, button):
        '''bti clicked handler'''
        # Clicking on a block adjacent to the blank block moves that
        # block to the blank space.
        blockNumber = int(button.text())
        position = self.puzzle.currentState.pattern.index(blockNumber)
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
            self.moveBlock(blockNumber, destination + 1)

    def createPuzzle(self):
        '''Creates a new puzzle.'''
        pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.puzzle = EightPuzzle(pattern)
        self.puzzle.shufflePuzzle()
        self.setTheBoard(self.puzzle.currentState.pattern)

    def randomizeHandler(self):
        '''btRand handler for shuffling the puzzle.'''
        self.puzzle.shufflePuzzle()
        self.clear_labels()
        self.setTheBoard(self.puzzle.currentState.pattern)

    def toggleButtons(self):
        '''Toggles the state of the buttons'''
        enable = self.btsol.isEnabled()
        self.btsol.setEnabled(enable)
        self.btrand.setEnabled(enable)
        for bt in self.btBlocks:
            if bt:
                bt.setEnabled(enable)

    def moveBlock(self, blockNumber, destination):
        '''Moves a block from blockNumber to destination'''
        # start and end are in range [1,9]. This function moves a block.
        geometryPositions = {0: (10, 10), 1: (60, 10), 2: (110, 10),
                             3: (10, 60), 4: (60, 60), 5: (110, 60),
                             6: (10, 110), 7: (60, 110), 8: (110, 110)}
        position = self.puzzle.currentState.pattern.index(blockNumber)
        x, y = geometryPositions[destination - 1]
        w, h = self.btBlocks[blockNumber - 1].width(), self.btBlocks[blockNumber - 1].height()
        self.btBlocks[blockNumber - 1].setGeometry(QRect(x, y, w, h))
        self.puzzle.currentState.swapBlocks(position, destination - 1)

    def setTheBoard(self, pattern):
        '''Presents the puzzle into the interface.'''
        for i, p in enumerate(pattern):
            if p != 9:
                self.moveBlock(p, i + 1)
