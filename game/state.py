class State:
    def __init__(self, pattern, cost=0, father=None):
        self.pattern = pattern
        self.heuristic = self.get_heuristic()
        self.cost = cost
        self.father = father

    def __str__(self):
        pattern = list(self.pattern)
        pattern[pattern.index(9)] = '-'
        return "{0} {1} {2}\n{3} {4} {5}\n{6} {7} {8}".format(pattern[0], pattern[1], pattern[2],
                                                              pattern[3], pattern[4], pattern[5],
                                                              pattern[6], pattern[7], pattern[8])

    def __getitem__(self, item):
        return self.pattern[item]

    def __setitem__(self, key, value):
        self.pattern[key] = value
        self.heuristic = self.get_heuristic()

    def get_successors(self):
        blank_index = self.pattern.index(9)
        blank_row = blank_index // 3
        blank_col = blank_index % 3
        successors = []
        if blank_row > 0:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blank_index], state[blank_index - 3] = state[blank_index - 3], state[blank_index]
            successors.append(state)
        if blank_row < 2:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blank_index], state[blank_index + 3] = state[blank_index + 3], state[blank_index]
            successors.append(state)
        if blank_col > 0:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blank_index], state[blank_index - 1] = state[blank_index - 1], state[blank_index]
            successors.append(state)
        if blank_col < 2:
            state = State(list(self.pattern), self.cost + 1, father=self)
            state[blank_index], state[blank_index + 1] = state[blank_index + 1], state[blank_index]
            successors.append(state)
        return successors

    def swap_blocks(self, i, j):
        self[i], self[j] = self[j], self[i]

    def goal_test(self):
        final = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if self[i] != final[i]:
                return False
        return True

    def get_heuristic(self):
        h = 0
        for i in range(9):
            if self[i] != 9:
                right_place = self[i] - 1
                current_place = i
                h += abs(right_place % 3 - current_place % 3) + abs(right_place // 3 - current_place // 3)
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
        pattern = self.pattern
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        index = 0
        for i in range(9):
            index += sum(p < pattern[i:][0] for p in pattern[i:]) * fact[len(pattern[i:]) - 1]
        return index

    def f(self):
        return self.heuristic + self.cost

