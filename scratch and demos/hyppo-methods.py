import numpy as np
from numpy import random
import matplotlib as plt
from hyppo import independence, tools


def combine_and_label(x1, x2):
    return_X = np.concatenate([x1, x2])

    n1 = x1.shape[0]
    n2 = x2.shape[0]

    return_Y = np.repeat([1, 2], [n1, n2])

    return return_X, return_Y

rng = random.default_rng()
mean = [0,0]
cov1 = [[1, 0],[0, 100]]
cov2 = [[1, -1],[-1, 1]]

x1 = rng.multivariate_normal(mean, cov1, 10)
x2 = rng.multivariate_normal(mean, cov2, 10)
x, y = combine_and_label(x1, x2)

stat, p = independence.FriedmanRafsky().test(x,y)
stat2 = independence.FriedmanRafsky().statistic(x,y)