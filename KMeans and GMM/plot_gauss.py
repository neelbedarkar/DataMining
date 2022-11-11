import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import multivariate_normal


def gauss2d(mu, sigma, to_plot=False):
    w, h = 100, 100

    std = [np.sqrt(sigma[0, 0]), np.sqrt(sigma[1, 1])]
    x = np.linspace(mu[0] - 3 * std[0], mu[0] + 3 * std[0], w)
    y = np.linspace(mu[1] - 3 * std[1], mu[1] + 3 * std[1], h)

    x, y = np.meshgrid(x, y)

    x_ = x.flatten()
    y_ = y.flatten()
    xy = np.vstack((x_, y_)).T

    normal_rv = multivariate_normal(mu, sigma)
    z = normal_rv.pdf(xy)
    z = z.reshape(w, h, order='F')

    if to_plot:
        plt.contourf(x, y, z.T)

    return z


MU = np.array([[0.90405015, 3.91712731],
       [2.34984409, 2.22635325],
       [2.72488742, 3.52342783]])
SIGMA = np.array(
    [[[0.55102984, 0.20653126],
        [0.20653126, 0.31771781]],
       [[0.29499113, 0.00514977],
        [0.00514977, 0.58621492]],
       [[0.63676514, 0.01587902],
        [0.01587902, 0.86305595]]])

for x in range(len(MU)):
    z = gauss2d(MU[x], SIGMA[x], True)

print()
plt.show()


