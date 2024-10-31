from pandas import DataFrame
import numpy as np
 

def ML_Estimator(data: DataFrame):
    return [data.mean(axis=0), data.var(axis=0)]


def Variance_Squaremat(var):
    diagonalMatrix = np.diag(var)
    return diagonalMatrix
