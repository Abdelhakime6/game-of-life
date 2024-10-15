import numpy as np
import cellpylib as cp
import matplotlib.pyplot as plt

initial_state = np.random.choice([0, 1, 0], size=(50, 50))
cellular_automaton = np.array(initial_state)

def custom_rule(neighbors, cell, time):
    total = np.sum(neighbors)
    return 1 if total == 3 or (cell == 1 and total == 2) else 0

cellular_automaton = cp.evolve(cellular_automaton, timesteps=100, 
                               apply_rule=custom_rule)
plt.figure(figsize=(10, 10))
plt.imshow(cellular_automaton, cmap='viridis', interpolation='nearest')
plt.axis('off')
plt.show()
