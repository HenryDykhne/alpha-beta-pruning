import scipy.signal
import numpy as np
import random
import time
import copy
from random import randrange
from TicTacToeState import TicTacToeState
from func_timeout import func_timeout, FunctionTimedOut
from WinConditions import win3, win4, win5, central3, central4, central5
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

    def central_squares(self, boardState):
        if boardState.sideLength == 3:
            center = central3
        elif boardState.sideLength == 4:
            center = central4
        elif boardState.sideLength == 5:
            center = central5
        else:
            return 0
        tot = 0
        for i, ring in enumerate(center):
            res = scipy.signal.convolve2d(boardState.grid, ring, mode='valid', boundary='fill', fillvalue=0)
            tot += (boardState.sideLength - i - 2) * res[0][0]
        return tot

    def winning_structures(self, boardState):
        xGrid = copy.deepcopy(boardState.grid)
        oGrid = copy.deepcopy(boardState.grid)
        np.place(xGrid, xGrid == 1, [0])
        np.place(oGrid, oGrid == -1, [0])
        if boardState.sideLength == 3:
            win = win3
        elif boardState.sideLength == 4:
            win = win4
        elif boardState.sideLength == 5:
            win = win5
        else:
            return None
        tot = 0
        for condition in win:
            # we run a convolution to try and find winning possibilities
            xRes = scipy.signal.convolve2d(xGrid, condition, mode='valid', boundary='fill', fillvalue=0)
            oRes = scipy.signal.convolve2d(oGrid, condition, mode='valid', boundary='fill', fillvalue=0)
            for iy, ix in np.ndindex(xRes.shape):
                if xRes[iy, ix] != 0 and oRes[iy, ix] != 0:
                    tot += 0
                else:
                    tot += xRes[iy, ix] + oRes[iy, ix]
        return tot

    def weak_utility(self, boardState):
        res = self.game_result(boardState)
        val = 0
        if res == 1:
            val += self.winVal
        if res == -1:
            val += -self.winVal
        if res == 0:
            return 0
        val += (10 * boardState.sideToMove) + (20 * self.central_squares(boardState))
        return val

    def strong_utility(self, boardState):
        res = self.game_result(boardState)
        val = 0
        if res == 1:
            val += self.winVal
        if res == -1:
            val += -self.winVal
        if res == 0:
            return 0
        val += (10 * boardState.sideToMove) + (30 * self.winning_structures(boardState))
        return val

    def random_ordering(self, boardState, moveList):
        random.shuffle(moveList)

    def get_sort_val(self, boardState, move):
        newState = self.make_move(boardState, move[0], move[1])
        if newState.hashValue in self.transpositionTable:
            return self.transpositionTable[newState.hashValue]
        else:
            return 0

    def lower_depth_eval_ordering(self, boardState, moveList):
        if boardState.sideToMove == 1:
            rev = True
        else:
            rev = False
        moveList.sort(key=lambda move: self.get_sort_val(boardState, move), reverse=rev)

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
        self.numNodesExplored += 1
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
                if tempVal > val:
                    val = tempVal
                    y = move[0]
                    x = move[1]
            return val, y, x
        elif boardState.sideToMove == -1:
            val = float('inf')
            for move in moves:
                newState = self.make_move(boardState, move[0], move[1])
                tempVal, ty, tx = self.minimax(newState, depth - 1)
                if tempVal < val:
                    val = tempVal
                    y = move[0]
                    x = move[1]
            return val, y, x

    def alpha_beta(self, boardState, depth, a, b):
        self.numNodesExplored += 1
        if depth == 0 or self.game_result(boardState) != None:
            if boardState.hashValue in self.transpositionTable:
                val = self.transpositionTable[boardState.hashValue]
            else:
                val = self.utility(boardState)
                self.transpositionTable[boardState.hashValue] = val
            return val, None, None
        moves = self.generate_moves(boardState)
        if depth != 1:
            self.ordering(boardState, moves)
        y, x = 0, 0
        if boardState.sideToMove == 1:
            val = float('-inf')
            for move in moves:
                newState = self.make_move(boardState, move[0], move[1])
                tempVal, ty, tx = self.alpha_beta(newState, depth - 1, a, b)
                if tempVal > val:
                    val = tempVal
                    y = move[0]
                    x = move[1]
                if val >= b:
                    break
                a = max(a, val)
            self.transpositionTable[boardState.hashValue] = val
            return val, y, x
        elif boardState.sideToMove == -1:
            val = float('inf')
            for move in moves:
                newState = self.make_move(boardState, move[0], move[1])
                tempVal, ty, tx = self.alpha_beta(newState, depth - 1, a, b)
                if tempVal < val:
                    val = tempVal
                    y = move[0]
                    x = move[1]
                if val <= a:
                    break
                b = min(b, val)
            self.transpositionTable[boardState.hashValue] = val
            return val, y, x

    def search_shell(self, boardState):
        self.numNodesExplored = 0
        depth = 1
        timeStart = time.perf_counter()
        val, y, x = 0,0,0
        thinkTime = 60 ## MAX NUMBER OF SECONDS TO THINK FOR
        timeLeft = thinkTime 
        limitExceeded = False
        while timeLeft > 0 and depth <= boardState.movesLeft:
            try:
                print("Searching depth (plies): " + str(depth) + " | Time Remaining: " + f'{timeLeft:.2f}' + ' seconds')
                if self.search == '2':
                    val, y, x = func_timeout(timeLeft, self.minimax, args=(boardState, depth))
                elif self.search == '3':
                    val, y, x = func_timeout(timeLeft, self.alpha_beta, args=(boardState, depth, float('-inf'), float('inf')))
            except FunctionTimedOut:
                limitExceeded = True
            depth += 1
            timeLeft = thinkTime - (time.perf_counter() - timeStart)
            if val >= self.winVal - 10000 or val <= -self.winVal + 10000:
                break
        if limitExceeded:
            print('Time limit exceeded. Search depth (plies) completed: ' + str(depth - 2))
        else:
            print('Search depth (plies) completed: ' + str(depth - 1))
        print('Nodes explored: ' + str(self.numNodesExplored) + ' | Wall clock time elapsed: ' + f'{(time.perf_counter() - timeStart):.2f}' + ' seconds')
        print('Eval: ' + str(val))
        return y, x

    def __init__(self, aiType, utility, ordering):
        if aiType == '1':
            self.move = self.random_move
        else:
            self.move = self.search_shell
            self.search = aiType

        if utility == '1':
            self.utility = self.weak_utility
        elif utility == '2':
            self.utility = self.strong_utility
        else:
            self.utility = None

        if ordering == '1':
            self.ordering = self.random_ordering
        elif ordering == '2':
            self.ordering = self.lower_depth_eval_ordering
        else:
            self.ordering = None
        self.transpositionTable = {}
        self.winVal = 10000000 #revert to float('inf') if this is causing problems

    