from time import sleep
import random
import numpy as np
#to wszystko do inputu potem
pr_or = 0 #proper_orientation  range 0-359 deg
cur_or = 0 #current_orientation range 0-359 deg
cur_til = 0 #current_tilt  range -max_tilt: max_tilt [deg]
max_til = 30 #[deg]
max_til_or_ch = 10 #max_tlt_induced_orientation_change   [deg]
max_tur_til = 3 #max_turbulence_tilt[deg]
max_or_cor = 10 #max_orintation_correction


while True:
    #to pewnie się da jakoś krócej napisać
    tur_til = (random.gauss(0, 1/3*max_tur_til))
    while abs(tur_til)>max_tur_til:
        tur_til = (random.gauss(0, 1 / 3 * max_tur_til))

    cur_til = (cur_til + tur_til if abs(cur_til + tur_til)<max_til else max_til*np.sign(cur_til + tur_til) )
    #orientation_change:
    or_ch = (max_til_or_ch/(max_til**2))*(cur_til**2)*np.sign(cur_til)
    #orientation_before_correction:
    or_bef_cor = cur_or + or_ch
    #orientation_error
    or_err = or_bef_cor - pr_or
    #orientation_correction:
    or_cor = (-max_or_cor*np.sin(np.pi/4*or_err/max_or_cor*1.1) if abs(or_err)<max_or_cor*1.1 else max_or_cor*(-np.sign(or_err)) )
    cur_or = or_bef_cor + or_cor

    print(
          f"tur_til = {tur_til}\n"
          f"cur_til = {cur_til}\n"
          f"orientation change = {or_ch}\n"
          f"or_bef_cor = {or_bef_cor}\n"
          f"or_err = {or_err}\n"
          f"or_cor ={or_cor}\n"
          f"current orientation = {cur_or}\n"
         )
    sleep(20)