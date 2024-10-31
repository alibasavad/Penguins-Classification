from scipy.stats import multivariate_normal
import statistics


def ClassifierAccuracy(dataset, realClass, M_Adelie, V_Adelie, M_Gentoo, V_Gentoo, M_Chinstrap, V_Chinstrap):
    dist_Adelie = multivariate_normal(M_Adelie, V_Adelie)
    dist_Gentoo = multivariate_normal(M_Gentoo, V_Gentoo)
    dist_Chinstrap = multivariate_normal(M_Chinstrap, V_Chinstrap)

    rightClassification = 0

    for x in dataset:
        if realClass == "Adelie":
            if dist_Adelie.pdf(x) == max(dist_Adelie.pdf(x), dist_Gentoo.pdf(x), dist_Chinstrap.pdf(x)):
                rightClassification += 1
        if realClass == "Gentoo":
            if dist_Gentoo.pdf(x) == max(dist_Adelie.pdf(x), dist_Gentoo.pdf(x), dist_Chinstrap.pdf(x)):
                rightClassification += 1
        if realClass == "Chinstrap":
            if dist_Chinstrap.pdf(x) == max(dist_Adelie.pdf(x), dist_Gentoo.pdf(x), dist_Chinstrap.pdf(x)):
                rightClassification += 1

    return rightClassification / len(dataset)


def MeanAccuracy(datasets, means, vars):
    A = ClassifierAccuracy(datasets[0], "Adelie", means[0],
                           vars[0], means[1], vars[1], means[2], vars[2])
    G = ClassifierAccuracy(datasets[1], "Gentoo", means[0],
                           vars[0], means[1], vars[1], means[2], vars[2])
    C = ClassifierAccuracy(datasets[2], "Chinstrap", means[0],
                           vars[0], means[1], vars[1], means[2], vars[2])

    return float("%.2f" % statistics.mean([A, G, C]))
