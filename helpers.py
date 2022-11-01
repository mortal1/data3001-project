import numpy as np

def vectorise(x):
    return np.array(x).reshape((-1, 1))


def diff_matrix(A):
    M = np.outer(np.ones_like(A), A)
    return M - M.T

