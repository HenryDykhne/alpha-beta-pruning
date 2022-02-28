import scipy.signal
import numpy as np
from random import randrange
from WinConditions import win3, win4, win5
class AI:
    def __init__(self, aiType, utility, ordering):
        self.aiType = aiType
        self.utility = utility
        self.ordering = ordering

    def random_move(self, boardState):
        result = np.where(boardState.grid == 0)
        randIndex = randrange(result[0].size)
        return result[0][randIndex], result[1][randIndex]

    def move(self, boardState):
        if self.aiType == "1":
            y,x = self.random_move(boardState)
        return y,x

    def game_result(self, currentState):
        if currentState.sideLength == 3:
            win = win3
        elif currentState.sideLength == 4:
            win = win4
        elif currentState.sideLength == 5:
            win = win5
        else:
            return None
        for condition in win:
            # we run a convolution to try and find a match
            res = scipy.signal.convolve2d(currentState.grid, condition, mode='valid', boundary='fill', fillvalue=0)
            if any(currentState.sideLength in sub for sub in res): #here we check for 1 winning
                return 1
            elif any(-currentState.sideLength in sub for sub in res):
                return -1
        if not any(0 in subl for subl in currentState.grid):
            return 0
        return None