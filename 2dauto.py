import numpy as np
import cellpylib as cp
import matplotlib.pyplot as mplt
import matplotlib.animation as man

cellular_automaton = cp.init_simple2d(60, 60)
cellular_automaton[:, [28,29,30,30], [30,31,29,31]] = 1
cellular_automaton[:, [40,40,40], [15,16,17]] = 1
cellular_automaton[:, [18,18,19,20,21,21,21,21,20], [45,48,44,44,44,45,46,47,48]] = 1



cellular_automaton = cp.evolve2d(cellular_automaton, timesteps=60, memoize='recursive', neighbourhood='Moore', apply_rule = cp.game_of_life_rule)

cp.plot2d_animate(cellular_automaton)
