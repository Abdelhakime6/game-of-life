import numpy as np
import cellpylib as cp
import matplotlib.pyplot as plt

# Initialize a cellular automaton with a single central cell
cellular_automaton = np.array([[1]*50 + [0]*10 + [1]*50 + [1]*50 + [0]*10 + [1]*50])

# Evolve the cellular automaton using Rule 110 for 100 timesteps
cellular_automaton = cp.evolve(cellular_automaton, timesteps=100, memoize=True,
                               apply_rule=lambda n, c, t: cp.nks_rule(n, rule=110))

# Plot the cellular automaton
plt.figure(figsize=(10, 10))
plt.imshow(cellular_automaton, cmap='plasma', interpolation='nearest')
plt.axis('off')
plt.show()
