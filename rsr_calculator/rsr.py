from math import exp, sqrt
from .version import version

MODE_1 = 1
MODE_2 = 2


class RSR(object):

    def __init__(
        self, mode_data=None, tsys_data=100, vel_data=0.031
    ):
        if mode_data is None:
            raise Exception('The input parameters are incorrect')
        else:
            self.mode = mode_data

        self.tsys = tsys_data
        self.vel = vel_data

    def get_version(self):
        return version

    def get_outputs(self, freq_data, time_data, unit_data):
        self.frequency = freq_data
        if self.mode == MODE_1:
            if unit_data == 'mk':
                mk = self.calculate_mk(time_data)
                temperature = self.calculate_temperature(mk)
                return {"mk": mk, "temperature": temperature}
            elif unit_data == 'mjy':
                mjy = self.calculate_mjy(time_data)
                flux = self.calculate_flux(mjy)
                return {"mjy": mjy, "flux": flux}

        elif self.mode == MODE_2:
            if unit_data == 'temperature':
                temperature = self.calculate_temperature(time_data)
                mk = self.calculate_mk(temperature)
                return {"mk": mk, "temperature": temperature}
            elif unit_data == 'flux':
                flux = self.calculate_flux(time_data)
                mjy = self.calculate_mjy(flux)
                return {"mjy": mjy, "flux": flux}

    def calculate_mk(self, time_data):
        return (self.tsys/100)*(sqrt(100)/sqrt(self.calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def calculate_mjy(self, time_data):
        return 2.81*(self.tsys/100)*(sqrt(100)/sqrt(self.calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def calculate_temperature(self, time_data):
        return (10*self.tsys**2) /\
            (100*self.calculate_vel()*(time_data**2))

    def calculate_flux(self, time_data):
        return (78.961 * (self.tsys**2)) /\
            (100 * self.calculate_vel()*(time_data**2))

    def calculate_vel(self):
        return (299792.458*self.vel)/self.frequency

    def validate_frequency(self, freq_data):
        if freq_data >= 73 and freq_data <= 111:
            return True
        else:
            return False
