# config.py

# author: Neil Baker

### IMPORTS ###
import numpy as np

### INITIALIZE PARAMETERS -- MODIFY HERE ###
# basic parameters
N = 4                   # number of bodies (> 2)
dim = 1                 # dimension of the solve (1, 2 or 3)
dt = 1                  # temporal step (s)
Tmax =1e6               # max time (s)

# input body initial conditions
# ensure number of bodies matches N
# format is [m, r0, v0], where r0 and v0 are lists, even if in 1D
me = [100, [0], [0]]
moon = [1e22, [1e8], [0]]
earth = [1e24, [6.4e6], [0]]
earth2 = [1e24, [-6.4e6], [0]]
# combine all bodies into a list
bodies = [me, earth, earth2, moon]

# monitor conservation
track_energy_conservation = False
track_momentum_conservation = True

### INITIALIZE PARAMETERS -- DO NOT MODIFY ###
# calculated
t_num = int(Tmax/dt)

# indices for use in the solver
mass = 0
pos = 1
vel = 2
