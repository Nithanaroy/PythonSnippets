import numpy as np
from scipy.optimize import curve_fit


def func(x):
    return [0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 12, 26, 26, 54, 2695, 3275, 1133, 597, 410, 733]


xdata = [i for i in range(0, 20)]
ydata = func(xdata)
# ydata = y + 0.2 * np.random.normal(size=len(xdata))
popt, pcov = curve_fit(func, xdata, ydata)
print popt, pcov
