import imp
import math
from pydoc import describe
import numpy as np
import os
os.system('cls')

# Overall
total_mass = 10  # kg
g = 9.81        # gravity
side = 0.150    # side length (meter)

# Momentum wheel
thickness = 0.01       # meter
density = 7130      # kg/m^3 , cast iron
outer_diameter = 0.100     # meter
inner_diameter =0.080     # meter
wheel_inertia = 0.5*density*np.pi*(outer_diameter**4-inner_diameter**4)*thickness
wheel_mass = np.pi*(outer_diameter**2-inner_diameter**2)*thickness*density
print('Momentum wheel inertia',round(wheel_inertia,4),'kg m^2')
print('Momentum wheel mass',round(wheel_mass,2),'kg')

# Motor specification
torque = 0.0696      # N*m
acceletation = torque/wheel_inertia

# Transmission 
larger_gear = 1    # teeth number
smaller_gear = 1

# Conservation of energy
height_change = side*np.sqrt(2)/2       # Approximate as we don't know CM location

energy_required = total_mass * g * height_change    # Energy required
# print('energy',energy_required)

omega_required = np.sqrt(2*energy_required/wheel_inertia)
print('wheel rpm required',round(omega_required*60/(2*np.pi),2))

motor_speed_min = omega_required*larger_gear/smaller_gear

motor_rpm_min = motor_speed_min*60/(2*np.pi)
print('motor rpm required',round(motor_rpm_min,2))

time_to_min_speed = omega_required/acceletation
print('acceleration time',round(time_to_min_speed,2),'s')
