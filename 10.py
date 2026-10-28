import numpy as np
import random

# Ant Colony Optimization - Shortest Path

# Nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Distance Matrix
distance = np.array([
    [0, 2, 4, 0, 0, 0],  # A
    [2, 0, 1, 3, 0, 0],  # B
    [4, 1, 0, 0, 2, 0],  # C
    [0, 3, 0, 0, 1, 5],  # D
    [0, 0, 2, 1, 0, 2],  # E
    [0, 0, 0, 5, 2, 0]   # F
])

# ACO Parameters
num_ants = 20
iterations = 50

alpha = 1
beta = 2

evaporation = 0.5

# Initial Pheromone
pheromone = np.ones((6, 6))

# Source and Destination
source = 0        # A
destination = 5   # F

# Function to Find a Path
def find_path():

    current = source
    path = [current]

    while current != destination:

        # Find connected nodes
        neighbors = [
            i for i in range(6)
            if distance[current][i] > 0 and i not in path
        ]

        # No available path
        if not neighbors:
            return None

        # Calculate probabilities
        probabilities = []

        for next_node in neighbors:

            # Pheromone value
            tau = pheromone[current][next_node]

            # Heuristic value
            eta = 1 / distance[current][next_node]

            # Probability value
            probability = (
                (tau ** alpha) *
                (eta ** beta)
            )

            probabilities.append(probability)

        # Convert to NumPy array
        probabilities = np.array(probabilities)

        # Normalize probabilities
        probabilities = (
            probabilities /
            probabilities.sum()
        )

        # Select next node
        next_node = random.choices(
            neighbors,
            weights=probabilities,
            k=1
        )[0]

        # Add node to path
        path.append(next_node)

        # Move to next node
        current = next_node

    return path

# Best Path Variables
best_path = None
best_length = float('inf')

# ACO Main Iterations
for iteration in range(iterations):

    paths = []

    # Generate paths for all ants
    for ant in range(num_ants):

        path = find_path()

        if path is not None:

            # Calculate path length
            length = 0

            for i in range(len(path) - 1):
                length += distance[
                    path[i]
                ][
                    path[i + 1]
                ]

            # Store path and length
            paths.append((path, length))

            # Store best path
            if length < best_length:
                best_length = length
                best_path = path

    # Pheromone Evaporation
    pheromone *= (1 - evaporation)

    # Pheromone Deposit
    for path, length in paths:

        deposit = 1 / length

        for i in range(len(path) - 1):

            a = path[i]
            b = path[i + 1]

            pheromone[a][b] += deposit
            pheromone[b][a] += deposit

# Display Result
print("Ant Colony Optimization")
print("-----------------------")

print("Source :", nodes[source])
print("Destination :", nodes[destination])

print("Best Path :", end=" ")

for node in best_path:
    print(nodes[node], end=" ")

print()

print("Path Length :", best_length)