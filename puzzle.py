class Puzzle:
    def __init__(self, initialPositions, goalState):
        super().__init__()
        self.positions = initialPositions
        self.zero = initialPositions.index(0)
        self.goalState = goalState

    def down(self):
        if self.zero < 6:
            self.positions[self.zero] = self.positions[self.zero+3]
            self.positions[self.zero+3] = 0
            self.zero = self.zero+3
            return True
        else:
            return False

    def up(self):
        if self.zero > 2:
            self.positions[self.zero] = self.positions[self.zero-3]
            self.positions[self.zero-3] = 0
            self.zero = self.zero-3
            return True
        else:
            return False

    def left(self):
        if self.zero % 3 != 0:
            self.positions[self.zero] = self.positions[self.zero-1]
            self.positions[self.zero-1] = 0
            self.zero = self.zero-1
            return True
        else:
            return False

    def right(self):
        if self.zero % 3 != 2:
            self.positions[self.zero] = self.positions[self.zero+1]
            self.positions[self.zero+1] = 0
            self.zero = self.zero+1
            return True
        else:
            return False

    def isGoalState(self):
        if self.goalState == self.positions:
            print("Goal State is reached")
            print("---------------------------")
            return True
        return False

    def displayState(self):
        for i in range(0, 3):
            print(self.positions[i*3 + 0],self.positions[i*3+1], self.positions[i*3+2])
        print("---------------------------")
