from time import sleep
import random
import numpy as np
#to wszystko do inputu potem
proper_orientation = 0 #range 0-359 deg
current_orientation = 0 #range 0-359 deg
current_tilt = 0 #range -max_tilt: max_tilt [deg]
max_tilt = 30 #[deg]
max_tilt_induced_orientation_change = 10 #[deg]
max_turbulence_tilt = 3 #[deg]
max_orintation_correction = 10


while True:

    turbulence_tilt = (random.gauss(0, 1/3*max_turbulence_tilt))
    current_tilt = (current_tilt + turbulence_tilt if abs(current_tilt + turbulence_tilt)<max_tilt else max_tilt*np.sign(current_tilt + turbulence_tilt) )
    orientation_change = (max_tilt_induced_orientation_change/(max_tilt**2))*(current_tilt**2)*np.sign(current_tilt)

    orientation_before_correction = current_orientation + orientation_change
    orientation_error = proper_orientation-orientation_before_correction
    orientation_correction = (-orientation_error if abs(orientation_error)<max_orintation_correction else max_orintation_correction*(-np.sign(orientation_error)) )
    current_orientation = orientation_before_correction + orientation_correction

    print(f"orientation change = {orientation_change}\n orientation before correction = {orientation_before_correction}\n current orientation = {current_orientation}",)
    sleep(2)