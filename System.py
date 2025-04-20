# System.py

# author: Neil Baker

import numpy as np

import config as c
from Body import *

class System:
    """
    Constructs an object that can calculate of macrodata like energy and momentum, as well as 
    """

    def __init__(self, bodies):
        """
        Initializes the System class
        self.bodies: list of Body objects
        """
        self.bodies = bodies            
        self.size = len(self.bodies)    
        self.extent = None              # spatial domain of the interaction

    def initialize_acceleration(self):
        """
        Calculates the initial acceleration for all bodies
        """
        # loop through all bodies
        for i, body in enumerate(self.bodies):
            # isolate the body we want to update
            b = self.bodies[i]
            # remove it from the list
            self.bodies.remove(b)
            # get initial acceleration
            b.acceleration_1D(self.bodies, 0)
            # put it back
            self.bodies.insert(i, b)

    def next_step_1D(self, t):
        """
        Calculates the next step at time index t
        """

        # loop through self.bodies and calculate new position and velocity
        for i, body in enumerate(self.bodies):
            # isolate and remove
            b = self.bodies[i]
            self.bodies.remove(b)
            # calculate position, velocity
            b.euler_1D(self.bodies, t)
            # put it back
            self.bodies.insert(i, b)

        # loop through self.bodies again and calculate new accelerations
        for i, body in enumerate(self.bodies):
            # isolate and remove
            b = self.bodies[i]
            self.bodies.remove(b)
            # calculate acceleration
            b.acceleration_1D(self.bodies, t)
            # put it back
            self.bodies.insert(i, b)

    # def energy_conservation(self):
    #     """
    #     Calculates and returns the total system energy for each time step 
    #     """
    #     energy_list = []
    #     # loop through time
    #     for t in range(c.t_num+1):
    #         E_i = 0
    #         # at each time, loop through bodies
    #         for i, body in enumerate(self.bodies):
    #             # the total energy is 1/2 m (v_x^2 + v_y^2 + v_z^2)
    #             for j in range(c.dim):
    #                 # add energy to E_i
    #                 E_i += 1/2 * body.m * body.v[t][j]**2
    #         # add energy to energy_list
    #         energy_list += [E_i]
    
    #     return energy_list

    def momentum_conservation(self):
        """
        Calculates and returns the total system momentum for each time step 
        """
        momentum_list = []
        # loop through time
        for t in range(c.t_num+1):
            p_t = [0 for d in range(c.dim)]
            # at each time, loop through bodies
            for i, body in enumerate(self.bodies):
                # for each body, loop over the dimension
                for d in range(c.dim):
                    # add momentum to p_t
                    p_t[d] += body.v[t][d]
            # add the momentum at time t to the total list
            momentum_list += [p_t]

        return momentum_list
