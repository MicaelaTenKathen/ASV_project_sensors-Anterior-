import numpy as np


def mean(array):
    mean = np.mean(array)
    std = np.std(array)
    return mean, std