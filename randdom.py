import numpy as np
import cellpylib as cp
import matplotlib.pyplot as mplt
import matplotlib.animation as man

cellular_automaton = cp.init_random2d(60, 60)


cellular_automaton = cp.evolve2d(cellular_automaton, timesteps=90, neighbourhood='Moore',
                                  apply_rule=cp.game_of_life_rule)

cp.plot2d_animate(cellular_automaton)