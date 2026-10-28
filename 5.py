Practical No. 5 - Implement Quasi-Newton Methods to Find the Local Maxima

import numpy as np
from scipy.optimize import minimize

# Function Whose Maximum is Required
def f(x):
  return -(x[0] - 3)**2 + 9

# To find maximum, minimize the negative of the function
def objective(x):
  return -f(x)

# Initial value
x0 = [0]

# Quasi-Newton Method: BFGS
result = minimize(objective, x0, method='BFGS')

# Display Result
print("Quasi-Newton Method (BFGS)")
print("--------------------------------")
print("Optimal x =", round(result.x[0], 4))
print("Maximum Value =", round(f(result.x), 4))
print("Number of Iterations =", result.nit)
print("Success =", result.success)