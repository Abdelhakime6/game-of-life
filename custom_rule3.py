import numpy as np
import cellpylib as cp
import matplotlib.pyplot as plt


class custom_rule(cp.BaseRule):
    def __call__(self, n, c, t):
        if n[1][1] == 0:
            if np.sum(n) == 2: 
                return 1
            else: 
                return 0
        else:
            if np.sum(n) - 1 == 3 or np.sum(n) - 1 == 4 :
                return 1
            else:
                return 0 


rule = custom_rule()

cellular_automaton = cp.init_simple2d(60, 60)
cellular_automaton[:, [28,29,30,30], [30,31,29,31]] = 1
cellular_automaton[:, [40,40,40], [15,16,17]] = 1
cellular_automaton[:, [18,18,19,20,21,21,21,21,20], [45,48,44,44,44,45,46,47,48]] = 1



cellular_automaton = cp.evolve2d(cellular_automaton, timesteps=250, memoize='recursive', neighbourhood='Moore', apply_rule = rule)

cp.plot2d_animate(cellular_automaton)