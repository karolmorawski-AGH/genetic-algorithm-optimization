import numpy as np

# Rosenbrock function formula
# Global minimum f(1,1) for n = 2, f(1,1,1) for n = 3 ...
# Search domain: -infinity < x_i < infinity
# Restrictions: 1 <= i <= n
def rosen(x):
    return sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)


# Rastrigin function formula
# Global minimum f(0, ... , 0) = 0
# Search domain: -5.12 < x_i < 5.12
def rastrigin(x):
    return np.sum(x * x - 10 * np.cos(2 * np.pi * x)) + 10 * np.size(x)