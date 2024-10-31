from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from pandas import DataFrame, concat
from numpy import ndarray


def Normalize_Data(data: DataFrame, features: list):
    values = data.loc[:, features].values
    return StandardScaler().fit_transform(values)


def PCA_Transform(data: ndarray, prematureData):
    principalComponents = PCA(n_components=2).fit_transform(data)

    principalDF = DataFrame(data=principalComponents, columns=[
                            'principal component 1', 'principal component 2'])

    finalDf = concat([prematureData[['species']], principalDF], axis=1)

    return finalDf
