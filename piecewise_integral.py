import numpy as np
from matplotlib import pyplot as plt

def PolyCoefficients(x, coefficents):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.
    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """

    order = len(coefficents)
    y = 0

    for i in range(order):
        coefficent = coefficents[i]
        y += coefficent * (x ** i)
  
    return y

x = np.linspace(-100, 100, 100)
coefficents = [0, 0, 1]

plt.plot(x, PolyCoefficients(x, coefficents))
plt.show()
