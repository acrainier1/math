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

def copy_func(f):
    """
    Creates a deep copy of a function.
    """
    # Create a new function object using the original function's code and globals
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__, 
                           argdefs=f.__defaults__, closure=f.__closure__)
    
    # Update the new function's wrapper to preserve metadata
    g = functools.update_wrapper(g, f)
    
    # Explicitly copy the function's __dict__ to duplicate any custom attributes
    g.__dict__ = copy.deepcopy(f.__dict__)
    
    return g


f = lambda x: x ** 2
a = 0
b = 5
# c = 0 # constant of integration
sub_intervals = 50
interval = b - a
# d = interval / sub_intervals # interval width

precision = 100000
x_domain = np.linspace(-10, 10, precision)
coefficents = [0, 0, 1]
f_function = PolyCoefficients(x_domain, coefficents)


# FUNCTION PLOT
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
ax1.set_title('Function')
ax1.plot(x_domain, f_function)

# INTEGRAL PLOT
ax2.set_title('Integral')
ax2.plot(x_domain, PolyCoefficients(x_domain, [0, 0, 0, 1/3]))

integral = lambda x: (1/3) * (x ** 3)
area_under_curve = integral(b) - integral(a)
computed_areas = [0]
print('True area under curve:\n', area_under_curve)

# F_i_minus_1 = lambda x: f(a) * x  + c
# F_i = lambda x: x
# print('a:', a, ' b:',  b, ' c:', c)
# print('==========\n')

for s in range(1, sub_intervals):
    c = 0 # constant of integration
    F_i_minus_1 = lambda x: f(a) * x  + c
    F_i = lambda x: x
    d = interval / s # interval width

    for i in range(1, s):
        p = a + (i * d)
        c = F_i_minus_1(p)
        F_i = lambda x: f(p) * (x - a - (i * d)) + c

        value = F_i(p)
        # print(i, p, c, value)

        subinterval = i
        point = a + (subinterval * d)
        F_i_minus_1 = lambda x: f(point) * (x - a - (subinterval * d)) + c
        # print('==========\n')

    computed_areas.append(F_i(b))
    # print('Computed area under curve:\n', F_i(b))

computed_x_axis = list(range(sub_intervals))
area_under_curve_constant = [area_under_curve] * sub_intervals
# difference_in_areas = [a - b for a, b in zip(computed_areas, area_under_curve_constant)]

ax3.set_title('True area vs computed areas under curve')
ax3.set_xlabel('Number of subintervals')
ax3.plot(computed_x_axis, area_under_curve_constant, color='#4444AA')
ax3.plot(computed_x_axis, computed_areas, color='#FFA500')
# ax3.plot(computed_x_axis, difference_in_areas, color='#44AA44')
# ax3.spines['left'].set_position('center')
# ax3.spines['bottom'].set_position('center')



# INTEGRAL SEGMENTS
# a = domain / sub_intervals # interval width
# c = 0 # y intercept
# F_i_minus_1 = PolyCoefficients(x_domain, [c])
# print('domain:', domain, 'width a:', a)

# for i in range(0, sub_intervals):
#     ia = int(i * (precision / sub_intervals))
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
#     for i in range(0, sub_intervals):
#         a = x_start + (i * width)
#         b = a + width
#         # print('a, b:', a, b)
#         linspace_segment = int(i * (precision / sub_intervals))
#         slope_f_x = f_function[linspace_segment]
#         # print('slope_f_x:', slope_f_x)
#         integral_piece = AntiDerivativePolyCoefficients(x_domain, [c, slope_f_x], a, b)
#         ax1.plot(x_domain, integral_piece, color=f"#FF{i % 10}500")