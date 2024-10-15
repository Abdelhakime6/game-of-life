import numpy as np
import cellpylib as cp
import matplotlib.pyplot as plt

cell= np.sym.choice([0,1,0,1,0,1], size=400)
cellular_automaton = np.array([cell])

cellular_automaton = cp.evolve(cellular_automaton, timesteps=100, memoize=True,
                               apply_rule=lambda n, c, t: cp.nks_rule(n, rule=110))

plt.figure(figsize=(30, 30))
plt.imshow(cellular_automaton, cmap='magma', interpolation='nearest')
plt.axis('off')
plt.show()
