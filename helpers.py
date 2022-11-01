import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def vectorise(x):
    return np.array(x).reshape((-1, 1))


def diff_matrix(A):
    M = np.outer(np.ones_like(A), A)
    return M - M.T


def save_colouring(A, filename):
    IOTA = np.arange(len(A))
    scores = MinMaxScaler().fit_transform(vectorise(A)).reshape((-1))

    df = pd.DataFrame()
    df['index'] = IOTA+1
    # df['score'] = [int(i*100) for i in scores]
    df['score'] = np.around(scores*100)
    df.to_csv(filename, sep='\t', header=False, index=False)