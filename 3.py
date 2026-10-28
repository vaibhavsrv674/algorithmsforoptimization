Practical No. 3 - Implement Quadratic Fit Search.


import numpy as np


def f(x):
    return (x - 2) ** 2


def golden_section_search(a, b, tolerance):
    golden_ratio = (np.sqrt(5) - 1) / 2

    x1 = b - golden_ratio * (b - a)
    x2 = a + golden_ratio * (b - a)

    f1 = f(x1)
    f2 = f(x2)

    while abs(b - a) > tolerance:

        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2

            x2 = a + golden_ratio * (b - a)
            f2 = f(x2)

        else:
            b = x2
            x2 = x1
            f2 = f1

            x1 = b - golden_ratio * (b - a)
            f1 = f(x1)

    minimum = (a + b) / 2

    print("Minimum point =", minimum)
    print("Minimum value =", f(minimum))


golden_section_search(0, 5, 0.001)