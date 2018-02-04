import numpy as np
from scipy import signal

X = np.array([1, 0.6, 0.2])
G = np.array([10, 0, 12, 8, 0])

S = signal.convolve(X, G)

print(S)