from time import sleep
import random
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("time: %(asctime)s\n %(message)s")
file_handler = logging.FileHandler("orientation_info.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Plane:

    max_til = 30  # max possible tilt [deg]
    max_til_or_ch = 10  # max tilt induced orientation change [deg]
    max_or_cor = 10  # max possible orientation correction [deg]

    def __init__(self, name, proper_orientation, current_orientation, current_tilt,):
        self.name = name
        self.pr_or = proper_orientation
        self.cur_or = current_orientation
        self.cur_til = current_tilt

    def __repr__(self):
        return "{}\ncurrent_orientation: {}\ncurrent tilt: {}\ndesired orientation: {}".format(self.name, self.cur_or, self.cur_til, self.pr_or)

    # tilt [deg] to orientation change [deg] function
    def tilt_to_or_change(self, tilt):
        orientation_change = self.max_til_or_ch / (np.pi / 2) * np.arcsin(tilt / self.max_til)
        return orientation_change

    # orientation correction [deg] to tilt after correction [deg] function
    def or_correction_to_tilt(self, orientation_correction):
        tilt = 0.1 * orientation_correction
        return tilt
    def include_turbulence_tilt(self, tur_til):
        self.cur_til = (self.cur_til + tur_til if abs(self.cur_til + tur_til) < self.max_til else self.max_til * np.sign(self.cur_til + tur_til))

    def change_orientation(self, orientation_change):
        self.cur_or += orientation_change

    @classmethod
    def calculate_orientation_correction(cls, orientation_error):
        orientation_correction = (-cls.max_or_cor * np.sin(np.pi / 2 * orientation_error / cls.max_or_cor * 1.1) if abs(
            orientation_error) < cls.max_or_cor * 1.1 else cls.max_or_cor * (-np.sign(orientation_error)))
        return orientation_correction


class Environment:

    def __init__(self, max_turbulence_tilt): # max_turbulence_tilt [deg]
        self.max_tur_til = max_turbulence_tilt

    def calculate_turbulence_tilt(self):
        turbulence_tilt = (random.gauss(0, 1/3*self.max_tur_til))
        while abs(turbulence_tilt)>self.max_tur_til:
            turbulence_tilt = (random.gauss(0, 1 / 3 * self.max_tur_til))
        return turbulence_tilt

def simulation_step_generator(E, P):
    turbulence_tilt = E.calculate_turbulence_tilt()
    P.include_turbulence_tilt(turbulence_tilt)
    orientation_change = P.tilt_to_or_change(P.cur_til)
    P.change_orientation(orientation_change)
    orientation_error = P.cur_or - P.pr_or
    orientation_correction = P.calculate_orientation_correction(orientation_error)
    P.cur_til = P.or_correction_to_tilt(orientation_correction)
    sleep(4)
    yield logger.info("{}\n".format(P))


if __name__ == "__main__":
    print("plane simulator was activated\norientation info is stored in orientation_info.log")
    P = Plane('Plane1', 0, 0, 0)
    E = Environment(3)

    while True:
        next(simulation_step_generator(E, P))