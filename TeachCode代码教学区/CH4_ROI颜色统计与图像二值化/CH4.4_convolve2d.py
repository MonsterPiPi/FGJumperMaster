import numpy as np
from scipy import signal


F = np.array([
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0]
])

H = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])


S = signal.convolve2d(F, H, boundary='wrap',mode='valid')

print(S)
