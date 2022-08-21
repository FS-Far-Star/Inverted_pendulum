# imports
import numpy as np

# system parameters
block_mass = 3  # kg
wheel_mass = 1  # kg
wheel_inertia = 5           # ???? how to measure? 
center_of_mass = [0,0.75]   # meters
dt = 0.001                  # frequency?

# gyroscope
rot_x = 0       # degrees
rot_y = 0
rot_z = 15  

# Recorder
omega_wheel = 0

# Calculations
torque = block_mass*np.sqrt(np.dot(center_of_mass))*np.cos(rot_z)
alpha = torque/wheel_inertia
omega_target = omega_wheel + alpha*dt