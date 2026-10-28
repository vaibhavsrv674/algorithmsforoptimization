import numpy as np
import matplotlib.pyplot as plt

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel

# Objective function
def objective_function(x):
    return x**2 + np.sin(x)

# Training Data
X = np.array([
    -4, -3, -2, -1, 0, 1, 2, 3, 4
]).reshape(-1, 1)

# Calculate Function Values
y = objective_function(X.ravel())

# Create Gaussian Process Kernel
kernel = ConstantKernel(1.0) * RBF(
    length_scale=1.0
)

# Create Gaussian Process Model
model = GaussianProcessRegressor(
    kernel=kernel,
    random_state=42
)

# Train the Model
model.fit(X, y)

# Test Points
X_test = np.linspace(
    -5,
    5,
    100
).reshape(-1, 1)

# Make Predictions
y_pred, y_std = model.predict(
    X_test,
    return_std=True
)

# Display Predictions
print("Gaussian Process Surrogate Model")
print("--------------------------------")

test_values = [-3.5, -1.5, 0.5, 1.5, 3.5]

for x in test_values:

    prediction, uncertainty = model.predict(
        [[x]],
        return_std=True
    )

    print("x =", x)
    print("Predicted Value =", prediction[0])
    print("Uncertainty =", uncertainty[0])
    print()

# Plot Actual Function
plt.plot(
    X_test,
    objective_function(X_test.ravel()),
    label="Actual Function"
)

# Plot GP Prediction
plt.plot(
    X_test,
    y_pred,
    label="GP Prediction"
)

# Plot 95% Confidence Interval
plt.fill_between(
    X_test.ravel(),
    y_pred - 2 * y_std,
    y_pred + 2 * y_std,
    alpha=0.2,
    label="95% Confidence Interval"
)

# Plot Training Data
plt.scatter(
    X,
    y,
    label="Training Data"
)

# Labels and Title
plt.xlabel("X")
plt.ylabel("Function Value")
plt.title("Gaussian Process Surrogate Model")

plt.legend()
plt.grid(True)

plt.show()