# -*- coding: utf-8 -*-
from math import exp, sqrt
from .version import version


class RSR(object):
    """RSR.

    Class that allow us to obtain observation time.
    """

    MODE_1 = 1
    MODE_2 = 2
    T_SYS = 100
    VEL = 0.031

    def __init__(self, mode_data=None):
        """Construct RSR object.

        Keyword arguments:
        mode_data -- Calculator mode (default None)
        """
        if mode_data is None:
            raise Exception('The input parameters are incorrect')
        else:
            self.mode = mode_data

    def get_version(self):
        """Version.

        Get the module version.
        """
        return version

    def calculator(self, freq_data, time_data, unit_data):
        """calculator.

        Keyword arguments:
        freq_data -- frequency 73 and 111 GHz
        time_data -- time observing
        unit_data -- unit (mk,mjy or temperature, flux)

        return a dict
        """
        self.frequency = freq_data
        if self.mode == self.MODE_1:
            if unit_data == 'mk':
                mk = self.calculate_mk(time_data)
                temperature = self.calculate_temperature(mk)
                return {"mk": mk, "temperature": temperature}
            elif unit_data == 'mjy':
                mjy = self.calculate_mjy(time_data)
                flux = self.calculate_flux(mjy)
                return {"mjy": mjy, "flux": flux}

        elif self.mode == self.MODE_2:
            if unit_data == 'temperature':
                temperature = self.calculate_temperature(time_data)
                mk = self.calculate_mk(temperature)
                return {"mk": mk, "temperature": temperature}
            elif unit_data == 'flux':
                flux = self.calculate_flux(time_data)
                mjy = self.calculate_mjy(flux)
                return {"mjy": mjy, "flux": flux}

    def calculate_mk(self, time_data):
        """mk unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return (self.T_SYS/100)*(sqrt(100)/sqrt(self.calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def calculate_mjy(self, time_data):
        """mjy unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return 2.81*(self.T_SYS/100)*(sqrt(100)/sqrt(self.calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def calculate_temperature(self, time_data):
        """temperature unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return (10*self.T_SYS**2) /\
            (100*self.calculate_vel()*(time_data**2))

    def calculate_flux(self, time_data):
        """flux unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return (78.961 * (self.T_SYS**2)) /\
            (100 * self.calculate_vel()*(time_data**2))

    def calculate_vel(self):
        """Calculate Increase in speed.

        return a float
        """
        return (299792.458*self.VEL)/self.frequency

    def validate_frequency(self, freq_data):
        """validate frequency.

        Keyword arguments:
        freq_data -- frequency 73 and 111 GHz

        return a boolean
        """
        if freq_data >= 73 and freq_data <= 111:
            return True
        else:
            return False
