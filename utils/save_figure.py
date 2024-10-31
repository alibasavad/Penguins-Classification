import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import numpy as np


def Save_Figure_3_Class(data, name, xLabel, yLabel, title):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(xLabel, fontsize=15)
    ax.set_ylabel(yLabel, fontsize=15)
    ax.set_title(title, fontsize=20)

    species = ['Adelie', 'Gentoo', 'Chinstrap']
    colors = ['r', 'g', 'b']
    for target, color in zip(species, colors):
        indicesToKeep = data['species'] == target
        ax.scatter(data.loc[indicesToKeep, 'principal component 1'],
                   data.loc[indicesToKeep, 'principal component 2'], c=color, s=50)
    ax.legend(species)
    ax.grid()
    plt.gca().invert_yaxis()

    fig.savefig(f"{name}")


def Save_Contour_Figure_3_Class(datas: list, means: list, vars: list, name, xLabel, yLabel, title):
    priors = np.array([151/342, 123/342, 68/342])

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(xLabel, fontsize=15)
    ax.set_ylabel(yLabel, fontsize=15)
    ax.set_title(title, fontsize=20)

    species = ['Adelie', 'Gentoo', 'Chinstrap']
    colors = ['r', 'g', 'b']
    dists = []

    for color, mean, var, data in zip(colors, means, vars, datas):

        x = np.linspace(data[:, 0].min(), data[:, 0].max(), 100)
        y = np.linspace(data[:, 1].min(), data[:, 1].max(), 100)
        X, Y = np.meshgrid(x, y)
        pos = np.dstack((X, Y))

        rv = multivariate_normal(mean, var)
        Z = rv.pdf(pos)

        dists.append(rv)

        plt.contour(X, Y, Z, colors=color, levels=4)

        ax.scatter(data[:, 0], data[:, 1], c=color, s=50)

    # minX = []
    # maxX = []
    # minY = []
    # maxY = []

    # [minX.append(data[:, 0].min()) for data in datas]
    # [maxX.append(data[:, 0].max()) for data in datas]
    # [minY.append(data[:, 1].min()) for data in datas]
    # [maxY.append(data[:, 1].max()) for data in datas]

    # x = np.linspace(min(minX), max(maxX), 100)
    # y = np.linspace(min(minY), max(maxY), 100)
    # X, Y = np.meshgrid(x, y)
    # pos = np.dstack((X, Y))

    # pdfs = [dist.pdf(pos) for dist in dists]

    # posteriors = pdfs * priors[:, np.newaxis, np.newaxis]
    # posteriors /= posteriors.sum(axis=0)

    # class_map = np.argmax(posteriors, axis=0)
    # plt.contour(X, Y, class_map, colors="black", linewidths=0.4)

    ax.legend(species)
    ax.grid()
    plt.gca().invert_yaxis()

    fig.savefig(f"{name}")


def Save_Figure_1_Class(data, className, name, xLabel, yLabel, title):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(xLabel, fontsize=15)
    ax.set_ylabel(yLabel, fontsize=15)
    ax.set_title(title, fontsize=20)

    plt.gca().invert_yaxis()

    species = className

    if (className == "Adelie"):
        colors = "r"
    if (className == "Gentoo"):
        colors = "g"
    if (className == "Chinstrap"):
        colors = "b"

    ax.scatter(data['principal component 1'],
               data['principal component 2'], c=colors, s=50)
    ax.legend(species)
    ax.grid()

    fig.savefig(f"{name}")


def save(Data_2D, Data_2D_Unnormal):
    # unnormal data
    Save_Figure_3_Class(Data_2D_Unnormal, "2_Dimentional_Component_Unnormal", 'Principal Component 1',
                        'Principal Component 2', "2_Dimentional_Component_Unnormal")

    Save_Figure_1_Class(Data_2D_Unnormal.loc[Data_2D_Unnormal["species"] == "Adelie"], "Adelie", "2_Dimentional_Component_Adelie_Unnormal",
                        'Principal Component 1', 'Principal Component 2', "2_Dimentional_Component_Adelie_Unnormal")

    Save_Figure_1_Class(Data_2D_Unnormal.loc[Data_2D_Unnormal["species"] == "Chinstrap"], "Chinstrap", "2_Dimentional_Component_Chinstrap_Unnormal",
                        'Principal Component 1', 'Principal Component 2', "2_Dimentional_Component_Chinstrap_Unnormal")

    Save_Figure_1_Class(Data_2D_Unnormal.loc[Data_2D_Unnormal["species"] == "Gentoo"], "Gentoo", "2_Dimentional_Component_Gentoo_Unnormal",
                        'Principal Component 1', 'Principal Component 2',  "2_Dimentional_Component_Gentoo_Unnormal")

    # normal data

    Save_Figure_3_Class(Data_2D, "2_Dimentional_Component", 'Principal Component 1',
                        'Principal Component 2', "2_Dimentional_Component")

    Save_Figure_1_Class(Data_2D.loc[Data_2D["species"] == "Adelie"], "Adelie", "2_Dimentional_Component_Adelie",
                        'Principal Component 1', 'Principal Component 2', "2_Dimentional_Component_Adelie")

    Save_Figure_1_Class(Data_2D.loc[Data_2D["species"] == "Chinstrap"], "Chinstrap", "2_Dimentional_Component_Chinstrap",
                        'Principal Component 1', 'Principal Component 2', "2_Dimentional_Component_Chinstrap")

    Save_Figure_1_Class(Data_2D.loc[Data_2D["species"] == "Gentoo"], "Gentoo", "2_Dimentional_Component_Gentoo",
                        'Principal Component 1', 'Principal Component 2',  "2_Dimentional_Component_Gentoo")

    # normal data contour

    # unnormal data contour
