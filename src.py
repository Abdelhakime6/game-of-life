import numpy as np
import cellpylib as cp
import matplotlib.pyplot as mplt
import matplotlib.animation as man

cellular_automaton = np.array([[0,0,0,1,0,0,0,1,0,0,1,1,1]])
cellular_automaton = cp.init_simple(30)

cellular_automaton = cp.evolve(cellular_automaton, timesteps=60, memoize=True,apply_rule=lambda n, c, t: cp.nks_rule(n, rule=30))

cp.plot(cellular_automaton)

fig, ax = mplt.subplots()
mat = ax.matshow(cellular_automaton, cmap = 'binary')
mplt.axis('off')

def animate(i):
    mat.set_data(cellular_automaton[:i+1])
    return[mat]
ani = man.FuncAnimation(fig, animate, frames=60, interval=50, blit=True, repeat=False)
mplt.show()