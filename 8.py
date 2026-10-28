import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Random Forest Surrogate Modelling

# Objective function
def objective_function(x):
    return x**2 + np.sin(x)

# Generate Sample Points
X = np.linspace(-5, 5, 30).reshape(-1, 1)

# Calculate Actual Function Values
y = objective_function(X.ravel())

# Create Random Forest Surrogate Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the Model
model.fit(X, y)

# Test Points
X_test = np.linspace(-5, 5, 200).reshape(-1, 1)

# Predict Using Surrogate Model
y_pred = model.predict(X_test)

# Display Predictions
print("Random Forest Surrogate Model")
print("-----------------------------")

test_values = [-4, -2, 0, 2, 4]

for x in test_values:

    prediction = model.predict([[x]])[0]
    actual = objective_function(x)

    print("x =", x)
    print("Actual Value =", actual)
    print("Predicted Value =", prediction)
    print()

# Plot Actual Function and Surrogate Model
plt.scatter(
    X,
    y,
    label="Sample Data"
)

plt.plot(
    X_test,
    objective_function(X_test.ravel()),
    label="Actual Function"
)

plt.plot(
    X_test,
    y_pred,
    label="Random Forest Surrogate"
)

plt.xlabel("X")
plt.ylabel("Function Value")
plt.title("Random Forest Surrogate Model")

plt.legend()
plt.grid(True)

plt.show()
