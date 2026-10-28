Practical No. 4 - Implement Gradient Descent

# Function
def f(x):
  return x**2

# Derivative of function
def gradient(x):
  return 2*x

# Initial value
x = 10

# Learning rate
learning_rate = 0.1

# Number of iterations
iterations = 10

print("Gradient Descent")

for i in range(iterations):
  grad = gradient(x)

  # Update x
  x = x - learning_rate * grad

  print("Iteration", i + 1, ": x =", round(x, 4),
    "f(x) =", round(f(x), 4))

print("\nMinimum value occurs approximately at x =", round(x, 4))