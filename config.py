# config.py

# author: Neil Baker

### IMPORTS ###
import numpy as np

### INITIALIZE PARAMETERS -- MODIFY HERE ###
# basic parameters
N = 2                   # number of bodies (> 2)
dim = 1                 # dimension of the solve (1, 2 or 3)
dt = 1                  # temporal step (s)
Tmax = 3e4              # max time (s)

# input body initial conditions
# ensure number of bodies matches N
# format is [m, r0, v0], where r0 and v0 are lists, even if in 1D
me = [100, [6.4e6], [0]]
moon = [1e22, [1e8], [0]]
earth = [1e24, [0], [0]]

# monitor conservation
track_energy_conservation = False
track_momentum_conservation = False

### INITIALIZE PARAMETERS -- DO NOT MODIFY ###
# calculated
t_num = int(Tmax/dt)

# combine all bodies into a list
bodies = [me, earth]

# indices for use in the solver
mass = 0
pos = 1
vel = 2
