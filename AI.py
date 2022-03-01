import scipy.signal
import numpy as np
import time
import copy
from random import randrange
from TicTacToeState import TicTacToeState
from func_timeout import func_timeout, FunctionTimedOut
from WinConditions import win3, win4, win5
class AI:

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

    def weak_utility(self, boardState):
        if self.game_result(boardState) == 1:
            return float('inf')
        if self.game_result(boardState) == -1:
            return float('-inf')
        if self.game_result(boardState) == 0:
            return 0
        return 0

    def strong_utility(self, boardState):
        return 0

    def random_ordering(self, boardState):
        return 0

    def lower_depth_eval_ordering(self, boardState):
        return 0

    def random_move(self, boardState):
        result = np.where(boardState.grid == 0)
        randIndex = randrange(result[0].size)
        return result[0][randIndex], result[1][randIndex]

    def make_move(self, currentState, y, x):
        grid = copy.deepcopy(currentState.grid)
        grid[y,x] = currentState.sideToMove
        return TicTacToeState(grid, currentState.sideLength, currentState.sideToMove * -1, currentState.movesLeft - 1)

    def generate_moves(self, boardState):
        result = np.where(boardState.grid == 0)
        return list(zip(result[0],result[1]))

    def minimax(self, boardState, depth):
        if depth == 0 or self.game_result(boardState) != None:
            if boardState.hashValue in self.transpositionTable:
                val = self.transpositionTable[boardState.hashValue]
            else:
                val = self.utility(boardState)
                self.transpositionTable[boardState.hashValue] = val
            return val, None, None
        moves = self.generate_moves(boardState)
        y, x = 0, 0
        if boardState.sideToMove == 1:
            val = float('-inf')
            for move in moves:
                newState = self.make_move(boardState, move[0], move[1])
                tempVal, ty, tx = self.minimax(newState, depth - 1)
                if tempVal >= val:
                    val = tempVal
                    y = move[0]
                    x = move[1]
            return val, y, x
        elif boardState.sideToMove == -1:
            val = float('inf')
            for move in moves:
                newState = self.make_move(boardState, move[0], move[1])
                tempVal, ty, tx = self.minimax(newState, depth - 1)
                if tempVal <= val:
                    val = tempVal
                    y = move[0]
                    x = move[1]
            return val, y, x

    def minimax_shell(self, boardState):
        depth = 1
        timeStart = time.perf_counter()
        val, y, x = 0,0,0
        timeLeft = 60
        while timeLeft > 0 and depth <= boardState.movesLeft:
            try:
                val, y, x = func_timeout(timeLeft, self.minimax, args=(boardState, depth))
                print("Depth: " + str(depth) + "Time Remaining: " + str(timeLeft))
            except FunctionTimedOut:
                pass
            depth += 1
            timeLeft = 60 - (time.perf_counter() - timeStart)
            if val == float('inf') or val == float('-inf'):
                break
        return y, x

    def alpha_beta(self, boardState, depth):
        return 0
    def alpha_beta_shell(self, boardState):
        return 0
    
    def __init__(self, aiType, utility, ordering):
        if aiType == '1':
            self.move = self.random_move
        elif aiType == '2':
            self.move = self.minimax_shell
        elif aiType  == '3':
            self.move = self.alpha_beta_shell
        else:
            self.move = None

        if utility == '1':
            self.utility = self.weak_utility
        elif utility == '2':
            self.utility = self.strong_utility
        else:
            self.utility = None

        if ordering == '1':
            self.ordering = self.random_ordering
        elif utility == '2':
            self.ordering = self.lower_depth_eval_ordering
        else:
            self.ordering = None
        self.transpositionTable = {}

    