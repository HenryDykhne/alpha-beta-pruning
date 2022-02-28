# win condition filters 3x3
vertWin3 = [[1],
            [1],
            [1]]
horWin3 = [[1,1,1]]
leftDiagWin3 = [[1,0,0],
                [0,1,0],
                [0,0,1]]
rightDiagWin3 = [[0,0,1],
                    [0,1,0],
                    [1,0,0]]
win3 = [vertWin3, horWin3, leftDiagWin3, rightDiagWin3]
# win condition filters 4x4
vertWin4 = [[1],
            [1],
            [1],
            [1]]
horWin4 = [[1,1,1,1]]
leftDiagWin4 = [[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]]
rightDiagWin4 = [[0,0,0,1],
                    [0,0,1,0],
                    [0,1,0,0],
                    [1,0,0,0]]
squareWin4 = [[1,1],
                [1,1]]
diamondWin4 = [[0,1,0],
                [1,0,1],
                [0,1,0]]
win4 = [vertWin4, horWin4, leftDiagWin4, rightDiagWin4, squareWin4, diamondWin4]
# win condition filters 5x5
vertWin5 = [[1],
            [1],
            [1],
            [1],
            [1]]
horWin5 = [[1,1,1,1,1]]
leftDiagWin5 = [[1,0,0,0,0],
                [0,1,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,0],
                [0,0,0,0,1]]
rightDiagWin5 = [[0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0]]
plusWin5 = [[0,1,0],
            [1,1,1],
            [0,1,0]]
leftBottomLWin5 = [[1,0,0],
                    [1,0,0],
                    [1,1,1]]
rightBottomLWin5 = [[0,0,1],
                    [0,0,1],
                    [1,1,1]]
leftTopLWin5 = [[1,1,1],
                [1,0,0],
                [1,0,0]]
rightTopLWin5 = [[1,1,1],
                    [0,0,1],
                    [0,0,1]]
win5 = [vertWin5, horWin5, leftDiagWin5, rightDiagWin5, leftDiagWin5, rightDiagWin5, plusWin5, leftBottomLWin5, rightBottomLWin5, leftTopLWin5, rightTopLWin5]
