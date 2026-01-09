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

def AntiDerivativePolyCoefficients(x, coefficents, a, b):
    y = PolyCoefficients(x, coefficents)

    for i, y_i in enumerate(y):
        if x[i] < a or x[i] >= b:
            y[i] = None

    return y


# FUNCTION
x_start = -10
x_end = 10
precision = 100000
x_domain = np.linspace(x_start, x_end, precision)
coefficents = [0, 0, 1]
f_function = PolyCoefficients(x_domain, coefficents)
domain = x_end - x_start
sub_intervals = 20
width = domain // sub_intervals
print('domain, width:', domain, width)

# INTEGRAL


# INTEGRAL PLOT
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)


for c in range(0, 1):
    print('\n===========\n')
    # print('c:', c)

    for i in range(0, sub_intervals):
        a = x_start + i * width
        b = a + width
        linspace_segment = int(i * (precision / sub_intervals))
        slope_f_x = f_function[linspace_segment]
        # print('a, b:', a, b)
        print('slope_f_x:', slope_f_x)
        integral_piece = AntiDerivativePolyCoefficients(x_domain, [c, slope_f_x], a, b)
        ax1.plot(x_domain, integral_piece, color=f"#FF{i % 10}500")
# FUNCTION PLOT
ax2.plot(x_domain, f_function)

plt.ylim(-10, 10)
plt.tight_layout()
plt.show()



# x_test = np.linspace(-1, 1, 100)
# y = 0
# for i in range(3):
#     y += 5 * (x_test ** 2)

# print('test:', x_test)
# print('\n===================\ny:', y)

# sub_domain = 0
# sub_domain += 5 * (x_test ** 2)
# c=0

# for i, x in enumerate(sub_domain):
#     if x < 0 or x >= 1:
#         sub_domain[i] = 0
#         c+=1

# print(len(x_test), len(sub_domain), c)
# print('\n===================\nsub_domain:', sub_domain)