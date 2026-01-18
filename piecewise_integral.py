import numpy as np
from matplotlib import pyplot as plt
import types
import functools
import copy

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

def PiecePolyCoefficients(x, y, a, i):
    left_endpoint = i * a
    right_endpoint = (i + 1) * a
    # print (left_endpoint, right_endpoint)

    for i, y_i in enumerate(y):
        if x[i] < left_endpoint or x[i] >= right_endpoint:
            y[i] = None

    return y


f = lambda x: x ** 2
a = 0
b = 5
precision = 1000
x_domain = np.linspace(-10, 10, precision)
coefficents = [0, 0, 1]
f_function = PolyCoefficients(x_domain, coefficents)


# FUNCTION PLOT
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1)
ax1.set_title('Function')
ax1.plot(x_domain, f_function)

# INTEGRAL PLOT
ax2.set_title('Integral')
ax2.plot(x_domain, PolyCoefficients(x_domain, [0, 0, 0, 1/3]))

integral = lambda x: (1/3) * (x ** 3)
area_under_curve = integral(b) - integral(a)
computed_areas = []
approximation_plots = []
interval = b - a
subintervals = 50
print('True area under curve:\n', area_under_curve)

for s in range(0, subintervals):
    c = 0 # constant of integration
    F_i_minus_1 = lambda x: f(a) * x  + c
    F_i = lambda x: x
    d = interval / (s + 1) # interval width
    plot_values = [F_i_minus_1(a)]

    for i in range(1, s + 1):
        p = a + (i * d)
        c = F_i_minus_1(p)
        F_i = lambda x: f(p) * (x - a - (i * d)) + c
        value = F_i(p)
        plot_values.append(value)
        subinterval = i
        point = a + (subinterval * d)
        F_i_minus_1 = lambda x: f(point) * (x - a - (subinterval * d)) + c

    computed_areas.append(F_i(b))
    approximation_plots.append(plot_values)

# Reinard Integral Approximation
partitioned_plot_values = []
subi = 50
breakpoint = precision // subi
print('==========\n')
print('breakpoint', breakpoint)
# print(approximation_plots)

j = 0

for i in range(0, precision):
    if i % breakpoint:
        partitioned_plot_values.append(None)
    else:
        # print('j', j)
        partitioned_plot_values.append(approximation_plots[subi - 1][j])
        try:
            partitioned_plot_values[i - 1] = approximation_plots[subi - 1][j]
        except IndexError as e:
            pass

        j += 1

# print(partitioned_plot_values)
ax2.plot(x_domain, partitioned_plot_values, color='#FF0000')

computed_x_axis = list(range(subintervals))
area_under_curve_constant = [area_under_curve] * subintervals

ax3.set_title('True area vs computed areas under curve')
ax3.set_xlabel('Number of subintervals')
ax3.plot(computed_x_axis, area_under_curve_constant, color='#4444AA')
ax3.plot(computed_x_axis, computed_areas, color='#FFA500')



# INTEGRAL SEGMENTS
# a = domain / subintervals # interval width
# c = 0 # y intercept
# F_i_minus_1 = PolyCoefficients(x_domain, [c])
# print('domain:', domain, 'width a:', a)

# for i in range(0, subintervals):
#     ia = int(i * (precision / subintervals))
#     slope_f_x = f_function[ia]

#     c = (-1 * slope_f_x) + F_i_minus_1[ia]
#     F_integral = PolyCoefficients(x_domain, [c, slope_f_x])
#     copy_F_integral = F_integral.copy()
#     integral_piece = PiecePolyCoefficients(x_domain, copy_F_integral, a, i)

#     ax1.plot(x_domain, integral_piece, color=f"#FF{i % 10}500")

#     F_i_minus_1 = F_integral


# plt.ylim(-10, 10)
plt.tight_layout()
plt.show()

# for c in range(-100, 100):
#     # print('\n===========\n')
#     # print('c:', c)
#     for i in range(0, subintervals):
#         a = x_start + (i * width)
#         b = a + width
#         # print('a, b:', a, b)
#         linspace_segment = int(i * (precision / subintervals))
#         slope_f_x = f_function[linspace_segment]
#         # print('slope_f_x:', slope_f_x)
#         integral_piece = AntiDerivativePolyCoefficients(x_domain, [c, slope_f_x], a, b)
#         ax1.plot(x_domain, integral_piece, color=f"#FF{i % 10}500")