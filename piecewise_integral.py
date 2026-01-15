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

def PiecePolyCoefficients(x, y, a, i):
    left_endpoint = i * a
    right_endpoint = (i + 1) * a
    # print (left_endpoint, right_endpoint)

    for i, y_i in enumerate(y):
        if x[i] < left_endpoint or x[i] >= right_endpoint:
            y[i] = None

    return y


# FUNCTION
x_start = 0
x_end = 5
precision = 100000
x_domain = np.linspace(x_start, x_end, precision)
coefficents = [0, 0, 1]
f_function = PolyCoefficients(x_domain, coefficents)
domain = x_end - x_start
sub_intervals = 500

area_under_curve = (1/3) * (x_end ** 3)
computed_areas = []
difference_in_areas = []
print(area_under_curve)

for i in range(0, sub_intervals):
    computed_area = 0
    computed_areas.append(computed_area)
    difference_in_areas.append(area_under_curve - computed_area)



# INTEGRAL PLOT
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

# ax1.plot(x_domain, PolyCoefficients(x_domain, [0, 0, 0, 1/3]))

integral_x_axis = list(range(sub_intervals))
ax1.plot(integral_x_axis, computed_areas, color='#FFA500')
ax1.plot(integral_x_axis, difference_in_areas, color='#00A500')


# INTEGRAL CALCULATION
a = domain / sub_intervals # interval width
c = 0 # y intercept
F_i_minus_1 = PolyCoefficients(x_domain, [c])
print('domain:', domain, 'width a:', a)

# for i in range(0, sub_intervals):
#     ia = int(i * (precision / sub_intervals))
#     slope_f_x = f_function[ia]

#     c = (-1 * slope_f_x) + F_i_minus_1[ia]
#     F_integral = PolyCoefficients(x_domain, [c, slope_f_x])
#     copy_F_integral = F_integral.copy()
#     integral_piece = PiecePolyCoefficients(x_domain, copy_F_integral, a, i)

#     ax1.plot(x_domain, integral_piece, color=f"#FF{i % 10}500")

#     F_i_minus_1 = F_integral


# FUNCTION PLOT
ax2.plot(x_domain, f_function)

plt.ylim(-10, 10)
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