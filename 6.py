Practical No. 6 - Implement the AdaGrad method with application, RMSprop and AdaDelta

import math

# Function: f(x) = x^2
# Gradient: f'(x) = 2x

x = 10.0
learning_rate = 1.0
epsilon = 1e-8
G = 0.0

print("AdaGrad Optimization")
print("--------------------")

for i in range(10):

  # Calculate Gradient
  gradient = 2 * x

  # Accumulate Squared Gradient
  G = G + gradient ** 2

  # Update x
  x = x - (learning_rate / (math.sqrt(G) + epsilon)) * gradient

  print("Iteration", i + 1,

    ": x =", round(x, 4),
    "f(x) =", round(x ** 2, 4))

print("\nFinal x =", round(x, 4))
print("Minimum value =", round(x ** 2, 4))