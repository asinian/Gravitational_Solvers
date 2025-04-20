# Mesh.py

# author: Neil Baker

### IMPORTS ###
import numpy as np

import config as c
import scipy.constants as const

### CLASS DEFINITION ###
class Body():
    """
    Superclass
    """

    def __init__(self, mass, r0, v0):
        """
        initializes the Body class
        """
        self.dim = c.dim                                # 1, 2 or 3 dimensions
        self.m = mass                                   # mass (kg)
        self.x = np.zeros((c.t_num+1, self.dim))        # stores the position variable (m)
        self.v = np.zeros((c.t_num+1, self.dim))        # stores the velocity variable (m/s)
        self.a = np.zeros((c.t_num+1, self.dim))        # stores the acceleration variable (m/s^2)

        # initialize position and velocity
        self.x[0,:] = r0
        self.v[0,:] = v0

### ONE DIMENSION ###
class Body_1D(Body):
    """
    Subclass of Body
    """

    def __init__(self, mass, r0, v0):
        """
        Initializes the subclass
        """
        super().__init__(mass, r0, v0)

    def acceleration_1D(self, bodies, t):
        """
        Returns the acceleration of self due to other bodies at time t using Euler Forward
        Body: the mass experiencing the acceleration
        bodies: the other masses contributing to Body's acceleration
        t: the current time index
        """
        # initialize the acceleration
        a = 0

        # iteratively add the influence of each other object
        for i, body in enumerate(bodies):
            # G * m_i
            constants = const.G * body.m
            # 1 / |x_i - x_j|**(3/2)
            scale_factor = 1 / abs(body.x[t] - self.x[t]) ** (3/2)
            # x_i - x_j
            vector = body.x[t] - self.x[t]
            # append the influence to a
            a += constants * scale_factor * vector

        # update acceleration at time t
        self.a[t,:] = a

    def euler_1D(self, bodies, t):
        """
        Calculates the next step of self due to other bodies at time t using Euler Forward
        Body: the mass experiencing the acceleration
        bodies: the other masses contributing to Body's acceleration
        t: the current time index
        """

        # calculate new position
        x_new = self.x[t-1] + c.dt * self.v[t-1]
        # update position
        self.x[t,:] = x_new

        # calculate new velocity 
        v_new = self.v[t-1] + c.dt * self.a[t-1]
        # update velocity
        self.v[t,:] = v_new

        # calculate new acceleration
        self.acceleration_1D(bodies, t)

### TWO DIMENSIONS ###
class Body_2D(Body):
    """
    Subclass of Body
    """

    def __init__(self, mass, r0, v0):
        """
        Initializes the subclass
        """
        super().__init__(mass, r0, v0)

    def acceleration_3D(self, bodies, t):
        """
        Returns the acceleration of Body1bon due to other bodies at time t using Euler Forward
        Body: the mass experiencing the acceleration
        bodies: the other masses contributing to Body's acceleration
        t: the current time index
        """

    def Euler_2D(self, bodies, t):
        """
        Calculates the next step of self due to other bodies at time t using Euler forward
        Body: the mass experiencing the acceleration
        bodies: the other masses contributing to Body's acceleration
        t: the current time index
        """
        
### THREE DIMENSIONS ###
class Body_3D(Body):
    """
    Subclass of Body
    """

    def __init__(self, mass, r0, v0):
        """
        Initializes the subclass
        """
        super().__init__(mass, r0, v0)

    def acceleration_3D(self, bodies, t):
        """
        Returns the acceleration of Body1bon due to other bodies at time t using Euler Forward
        Body: the mass experiencing the acceleration
        bodies: the other masses contributing to Body's acceleration
        t: the current time index
        """

    def Euler_3D(self, bodies, t):
        """
        Calculates the next step of self due to other bodies at time t using Euler forward
        Body: the mass experiencing the acceleration
        bodies: the other masses contributing to Body's acceleration
        t: the current time index
        """

### TESTING ###
if __name__ == '__main__':
    m1 = 1
    m2 = 2
    x01 = [1]
    x02 = [-1]
    v01 = [0]
    v02 = [0]

    b1 = Body_1D(m1, x01, v01)
    b2 = Body_1D(m2, x02, v02)

    # b1.acceleration_1D([b2], 0)
    # print(b1.a)

    # print(bodylist)
    # for i in range(len(bodylist)):
    #     if i == 1:
    #         b = bodylist[i]
    #         bodylist.remove(b)
    #         break
    # print(bodylist)
    # bodylist.insert(3, b)
    # print(bodylist)
