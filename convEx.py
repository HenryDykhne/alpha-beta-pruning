import scipy.signal

image = [[-1, 0, 1, -1],
         [-1, 1,-1, -1],
         [ 1, 1, 1, -1],
         [-1, 1, 1, -1]]

filter_kernel = [[1],
                 [1],
                 [1],
                 [1]]
filter_kernel2 = [[0,1,0],
                  [1,0,1],
                  [0,1,0]]

res = scipy.signal.convolve2d(image, filter_kernel,
                              mode='valid', boundary='fill', fillvalue=0)
print(res)

res = scipy.signal.convolve2d(image, filter_kernel2,
                              mode='valid', boundary='fill', fillvalue=0)
print(res)
