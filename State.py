class State:
    # This class simulates a state in the game.
    # Variables:    pattern
    #               heuristic
    #               cost
    #               father
    # Methods:      getSuccessors
    #               swapBlocks
    #               goalTest
    #               getHeuristic
    #               hash
    #               F
    def __init__(self, pattern, cost=0, father=None):
        # Each state has a pattern of the current position of blocks,a
        # cost for getting to it from the initial position, a heuristic
        # that estimates the number of moves to get to the goal from it
        # and a father to reference to the state that it came from. The
        # father reference is used to get the path to this node from
        # the initial position. Pattern is modeled as a list containing
        # 9 number 1 to 9 and 9 being the blank block.
        self.pattern = pattern
        self.heuristic = self.getHeuristic()
        self.cost = cost
        self.father = father

    def __str__(self):
        # A state is printed like the game map, in 3 row and 3 columns.
        pattern = list(self.pattern)
        pattern[pattern.index(9)] = '-'
        return "{0} {1} {2}\n{3} {4} {5}\n{6} {7} {8}".format(pattern[0], pattern[1], pattern[2],
                                                              pattern[3], pattern[4], pattern[5],
                                                              pattern[6], pattern[7], pattern[8])

    def __getitem__(self, item):
        # Accessing the state's pattern with [] for ease of access.
        return self.pattern[item]

    def __setitem__(self, key, value):
        # Changing the state's pattern by []for ease of access. The
        # heuristic value should be updated after changing the pattern.
        self.pattern[key] = value
        self.heuristic = self.getHeuristic()

    def getSuccessors(self):
        '''Returns the successors of this state'''
        # The position of 9 is computed and successors are built according
        # to it. The maximum of four successors will be computed and
        # returned.
        blankIndex = self.pattern.index(9)
        blankRow = blankIndex // 3
        blankCol = blankIndex % 3
        successors = []
        if blankRow > 0:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blankIndex], state[blankIndex - 3] = state[blankIndex - 3], state[blankIndex]
            successors.append(state)
        if blankRow < 2:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blankIndex], state[blankIndex + 3] = state[blankIndex + 3], state[blankIndex]
            successors.append(state)
        if blankCol > 0:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blankIndex], state[blankIndex - 1] = state[blankIndex - 1], state[blankIndex]
            successors.append(state)
        if blankCol < 2:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blankIndex], state[blankIndex + 1] = state[blankIndex + 1], state[blankIndex]
            successors.append(state)
        return successors

    def swapBlocks(self, i, j):
        '''Swaps 2 blocks of the currentState.'''
        self[i], self[j] = self[j], self[i]

    def goalTest(self):
        '''Returns True if this is the goal state, otherwise returns
        False'''
        final = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if self[i] != final[i]:
                return False
        return True

    def getHeuristic(self):
        '''Returns the heuristic of this state'''
        # This part computes the sum of the manhattan distance of each
        # block with its current position.
        h = 0
        for i in range(9):
            if self[i] != 9:
                rightPlace = self[i] - 1
                currentPlace = i
                h += abs(rightPlace % 3 - currentPlace % 3) + abs(rightPlace // 3 - currentPlace // 3)
        # This part enhances the heuristic by computing linear conflict.
        # Linear Conflict Tiles Definition: Two tiles tj and tk are in a
        # linear conflict if tj and tk are in the same line, the goal
        # positions of tj and tk are both in that line, tj is to the
        # right of tk and goal position of tj is to the left of the goal
        # position of tk.
        for i in range(9):
            for j in range(i, 9):
                if self[i] != 9 and self[j] != 9:
                    r1 = self[i] - 1
                    r2 = self[j] - 1
                    c1 = i
                    c2 = j
                    if c1 // 3 == c2 // 3 == r1 // 3 == r2 // 3 and (
                                (c1 % 3 > c2 % 3 and r1 % 3 < r2 % 3) or (c1 % 3 < c2 % 3 and r1 % 3 > r2 % 3)):
                        h += 2
                    elif c1 % 3 == c2 % 3 == r1 % 3 == r2 % 3 and (
                                (c1 // 3 > c2 // 3 and r1 // 3 < r2 // 3) or (c1 // 3 < c2 // 3 and r1 // 3 > r2 // 3)):
                        h += 2
        return h

    def hash(self):
        '''Returns the hash value of this state.'''
        # This function returns a hash value for the state. This can be
        # used for keeping track of the visited states. Another approach
        # is using set with average accessing time of O(1),But since the
        # states of 8 puzzle is reasonable enough for memory (363,000)
        # we use hashing to ensure the O(1) time.
        pattern = self.pattern
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        index = 0
        for i in range(9):
            index += sum(p < pattern[i:][0] for p in pattern[i:]) * fact[len(pattern[i:]) - 1]
        return index

    def F(self):
        '''Returns the F of this state.'''
        # The F parameter is used for A* and is the sum of cost and the
        # heuristic.
        return self.heuristic + self.cost

