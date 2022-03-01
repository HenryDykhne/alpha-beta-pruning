class TicTacToeState:
    def __init__(self, grid, sideLength, sideToMove, movesLeft):
        self.grid = grid
        self.sideLength = sideLength
        self.sideToMove = sideToMove
        self.hashValue = ''.join(str(e) for e in sum(self.grid.tolist(), []))
        self.movesLeft = movesLeft
