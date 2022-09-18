import time
from random import shuffle

import fibonacci_heap_mod as fh

from State import State


class EightPuzzle:
    def __init__(self, initial_pattern):
        self.currentState = State(initial_pattern)

    def solvable(self):
        state = self.currentState
        counter = 0
        for i in range(9):
            for j in range(i, 9):
                if state[i] != 9 and state[j] != 9 and state[i] > state[j]:
                    counter += 1
        return counter % 2 == 0

    def shuffle_puzzle(self):
        shuffle(self.currentState.pattern)
        while not self.solvable():
            shuffle(self.currentState.pattern)

    def a_star(self):
        start_time = time.time()
        visited = list(False for i in range(363000))
        queue = fh.Fibonacci_heap()
        queue.enqueue(self.currentState, self.currentState.F())
        visited[self.currentState.hash()] = True
        while True:
            current = queue.min().get_value()
            queue.dequeue_min()
            if current.goalTest():
                fin_time = time.time()
                return current, fin_time - start_time
            suc = current.getSuccessors()
            for s in suc:
                if not visited[s.hash()]:
                    visited[s.hash()] = True
                    queue.enqueue(s, s.cost + s.heuristic)

    def find_path(self, state):
        path = []
        while state.father is not None:
            path.insert(0, state)
            state = state.father
        path.insert(0, state)
        return path
