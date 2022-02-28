import scipy.signal
import numpy as np


image = [[-1,-1, 0],
         [ 0, 1, 1],
         [-1, 1, 1],]

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

res1 = scipy.signal.convolve2d(image, vertWin3, mode='valid', boundary='fill', fillvalue=0)
res2 = scipy.signal.convolve2d(image, horWin3, mode='valid', boundary='fill', fillvalue=0)
res3 = scipy.signal.convolve2d(image, leftDiagWin3, mode='valid', boundary='fill', fillvalue=0)
res4 = scipy.signal.convolve2d(image, rightDiagWin3, mode='valid', boundary='fill', fillvalue=0)

b1=np.sum(res1)
b2=np.sum(res2)
b3=np.sum(res3)
b4=np.sum(res4)

print(res1)
print(res2)
print(res3)
print(res4)
print(b1)
print(b2)
print(b3)
print(b4)
print(b1+b2+b3+b4-1)


