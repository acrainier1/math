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
        # print('x:', x)

    return y

def AntiDerivativePolyCoefficients(x, coefficents, x_i, width):
    y = PolyCoefficients(x, coefficents)
    return y


# FUNCTION
x_domain = np.linspace(-20, 20, 100000)
coefficents = [0, 0, 1]


# INTEGRAL


# INTEGRAL PLOT
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

for c in range(-1, 2, 1):
    x_i = 0
    width = 1.0
    integral_piece = AntiDerivativePolyCoefficients(x_domain, [c, 1, 0], x_i, width)
    ax1.plot(x_domain, integral_piece, color='#FFA500')

# FUNCTION PLOT
f_function = PolyCoefficients(x_domain, coefficents)
print('func:', f_function)
ax2.plot(x_domain, f_function)

plt.ylim(-10, 10)
plt.tight_layout()
# plt.show()

x_test = np.linspace(-1, 1, 100)
y = 0
for i in range(3):
    y += 5 * (x_test ** 2)

# print('test:', x_test)
# print('\n===================\ny:', y)

sub_domain = 0
sub_domain += 5 * (x_test ** 2)
c=0

for i, x in enumerate(sub_domain):
    if x < 0 or x >= 1:
        sub_domain[i] = 0
        c+=1

print(len(x_test), len(sub_domain), c)
print('\n===================\nsub_domain:', sub_domain)