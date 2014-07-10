import numpy as np
from numpy import *
import scipy as sp
from scipy import integrate
from scipy.integrate import simps


def fourier(x):
    f = 1 + sin(x) + 0.3*cos(9*x)
    return f

x0 = np.linspace(0.0, 2*pi, num=100);
''
f = fourier(x0);
print f
''
result = integrate.simps(f,x0)
print result
