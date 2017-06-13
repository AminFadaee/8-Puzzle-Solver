import time
from State import State
from random import shuffle
import fibonacci_heap_mod as fh


class EightPuzzle:
    # This class simulates the 8 puzzle.
    # Variables:    currentState
    # Methods:      findPath
    #               solvable
    #               shufflePuzzle
    #               AStar
    def __init__(self, initialPattern):
        # An 8 puzzle has a State object currentState representing the
        # state puzzle is currently in.
        self.currentState = State(initialPattern)

    def solvable(self):
        '''Returns true if the goal is reachable from currentState'''
        # Some states of the 8 Puzzle can't get to the goal state, for
        # detecting them we compute the inversion count of the current
        # state's pattern. This value has to be even for a state to be
        # solvable.
        state = self.currentState
        counter = 0
        for i in range(9):
            for j in range(i, 9):
                if state[i] != 9 and state[j] != 9 and state[i] > state[j]:
                    counter += 1
        return counter % 2 == 0

    def shufflePuzzle(self):
        '''Shuffles the currentState's Pattern'''
        # Instead of creating a new EightPuzzle object for a new game,
        # we can simply shuffle the pattern of the current state, but
        # when shuffling we should avoid creating an unreachable state.
        shuffle(self.currentState.pattern)
        while not self.solvable():
            shuffle(self.currentState.pattern)

    def AStar(self):
        '''Returns the minimum costing result from currenState and the
        time spent for computing it.'''
        # This part uses the A* algorithm to find the best solution for
        # the puzzle. The algorithm is accompanied by a priority queue
        # implemented by a fibonacci heap with inserting complexity of
        # O(1) and popping the minimum with O(logn). The fibonacci heap
        # mod by a third party is used here
        # (https://pypi.python.org/pypi/fibonacci-heap-mod).
        startTime = time.time()
        visited = list(False for i in range(363000))
        queue = fh.Fibonacci_heap()
        queue.enqueue(self.currentState, self.currentState.F())
        visited[self.currentState.hash()] = True
        while True:
            current = queue.min().get_value()
            queue.dequeue_min()
            if current.goalTest():
                finTime = time.time()
                return current, finTime - startTime
            suc = current.getSuccessors()
            for s in suc:
                if not visited[s.hash()]:
                    visited[s.hash()] = True
                    queue.enqueue(s, s.cost + s.heuristic)

    def findPath(self, state):
        '''Returns a list containing the states for getting from
        currentState to state.'''
        # When the goal state is reached by AStar the path to getting
        # to it from current node is computed using the father variale
        # in each states.
        path = []
        while (state.father != None):
            path.insert(0, state)
            state = state.father
        path.insert(0, state)
        return path
