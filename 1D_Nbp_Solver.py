# two_body_problem

# author: Neil Baker

### IMPORTS ###
import os
import numpy as np
import copy as cp
import time
import matplotlib.pyplot as plt

import config as c
from library import *
from plot import *
from Body import *
from System import *

### FUNCTIONS ###
def one_dimensional_Nbp():
    """
    solves the N-body problem in one dimension
    """
    # start clock
    start = time.time()

    # checks
    if c.N < 2:
        raise ValueError("N must be > 1")
    assert c.dim in [1, 2, 3], "the system dimension must be 1, 2 or 3"
    assert len(c.bodies) == c.N, "number of bodies does not match N"
    assert len(c.bodies[0][1]) == c.dim, "length of initial position vector does not match dimension"
    assert len(c.bodies[0][2]) == c.dim, "length of initial velocity vector does not match dimension"

    # initialize the bodies as objects
    print("Initializing bodies...")
    bodies = []
    for i, body in enumerate(c.bodies):
        if c.dim == 1:
            bodies += [Body_1D(body[c.mass], body[c.pos], body[c.vel])]
        elif c.dim == 2:
            bodies += [Body_2D(body[c.mass], body[c.pos], body[c.vel])]
        elif c.dim == 3:
            bodies += [Body_3D(body[c.mass], body[c.pos], body[c.vel])]

    # create system object
    S = System(bodies)
    # initialize acceleration
    S.initialize_acceleration()

    # main loop #
    print("Beginning simulation...")
    # two ways of tracking time
    t = 0                   
    t_index = 0               
    while t_index < c.t_num:

        # iterate time
        t_index += 1
        t += c.dt

        # calculate the next step
        S.next_step_1D(t_index)

    ### plot results ###
    print("Generating output...")
    # plot_xva_single(bodies)
    # plot_xva_all(bodies)
    plot_individual(bodies)

    # # conservation checks
    # if c.track_energy_conservation:
    #     energy_list = S.energy_conservation()
    #     plot_energy(energy_list)
    if c.track_momentum_conservation:
        momentum_list = S.momentum_conservation()
        plot_momentum(momentum_list)

    ### stop clock ###
    stop = time.time()
    time_elapsed = round(stop - start, 2)
    print(f"Process completed in {time_elapsed} seconds.")

### RUN SCRIPT ###
if __name__ == "__main__":
    one_dimensional_Nbp()