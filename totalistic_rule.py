import numpy as np
import cellpylib as cp
import matplotlib.pyplot as mplt
import matplotlib.animation as man

cellular_automaton = cp.init_simple2d(60, 60)


cellular_automaton = cp.evolve2d(cellular_automaton, timesteps=30, neighbourhood='Moore',
                                  apply_rule=lambda n, c, t: cp.totalistic_rule(n, k=2, rule=126))

cp.plot2d_animate(cellular_automaton)