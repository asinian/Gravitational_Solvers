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
        self.extent = None              # spatial domain of the interactionbelie

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