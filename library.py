# library.py
# helper functions for the gravitational solvers

# author: Neil Baker

### IMPORTS ###
import numpy as np
import scipy.constants as const

import config as c
# from Body import *

### FUNCTIONS ###
def energy(bodies, t):
    """
    calculates the total energy of the system at the time t
    """

    energy = 0
    for i, body in enumerate(bodies):
        v = body.v[t]
        energy += 1/2 * body.m * v**2

    return energy

    
