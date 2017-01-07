from math import exp, sqrt
from .version import version

MODE_1 = 1
MODE_2 = 2


class RSR(object):

    def __init__(self, mode_data=None, tsys_data=100, vel_data=0.031):
        if mode_data == MODE_1 or mode_data == MODE_2:
            self.mode = mode_data
        else:
            print('Error')
        self.tsys = tsys_data
        self.vel = vel_data
        self.frequency = None
        self.time = None

    def __call__(self, param_1, param_2):
        if self.mode == MODE_1:
            self.frequency = param_1
            self.time = param_2
            print(self.expected_given_time())
        elif self.mode == MODE_2:
            print(self.time_required_target())
        else:
            print('Error')

    def get_version(self):
        return version

    def expected_given_time(self):
        mk = (self.tsys/100)*(sqrt(100)/sqrt(self.calculate_vel())) \
            * sqrt(10) / sqrt(self.time)
        mjy = mk * 2.81
        d_mk = {"mk": mk}
        d_mjy = {"mjy": mjy}
        result = (d_mk, d_mjy)
        return result

    def time_required_target(self):
        temperature = (10*self.tsys**2) /\
            (100*self.calculate_vel()*(self.time**2))
        flux = (78.961 * (self.tsys**2)) /\
            (100 * self.calculate_vel()*(self.time**2))
        # print(100*self.calculate_vel()*self.time**2)

        return {"temperature": temperature, "flux": flux}

    def calculate_vel(self):
        return (299792.458*self.vel)/self.frequency
