# -*- coding: utf-8 -*-
"""RSR."""
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
            raise Exception(
                "The input parameters are incorrect {}".format(mode_data)
            )
        else:
            self._mode = mode_data

    def get_version(self):
        """Version.

        Get the module version.
        """
        return version

    def set_mode(self, mode_data):
        """Set Mode.

        Set mode
        """
        self._mode = mode_data

    def calculator(self, freq_data, time_data, unit_data):
        """calculator.

        Keyword arguments:
        freq_data -- frequency 73 and 111 GHz
        time_data -- time observing
        unit_data -- unit (mk,mjy or temperature, flux)

        return a dict
        """
        self.frequency = freq_data
        if self._mode == self.MODE_1:
            if unit_data == 'mK':
                mk = '{0:.2f}'.format(self._calculate_mk(time_data))
                return {'mK': mk}
            elif unit_data == 'mJy':
                mjy = '{0:.2f}'.format(self._calculate_mjy(time_data))
                return {'mJy': mjy}

        elif self._mode == self.MODE_2:
            if unit_data == 'temperature':
                time = '{0:.2f}'.format(self._calculate_temperature(time_data))
                return {'time': time}
            elif unit_data == 'flux':
                time = '{0:.2f}'.format(self._calculate_flux(time_data))
                return {'time': time}

    def _calculate_mk(self, time_data):
        """The mK unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return (self.T_SYS/100)*(sqrt(100)/sqrt(self._calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def _calculate_mjy(self, time_data):
        """The mJy unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return 2.81*(self.T_SYS/100)*(sqrt(100)/sqrt(self._calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def _calculate_temperature(self, time_data):
        """The temperature unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return (10*self.T_SYS**2) /\
            (100*self._calculate_vel()*(time_data**2))

    def _calculate_flux(self, time_data):
        """The flux unit.

        Keyword arguments:
        time_data -- time observing

        return a float
        """
        return (78.961 * (self.T_SYS**2)) /\
            (100 * self._calculate_vel()*(time_data**2))

    def _calculate_vel(self):
        """Calculate Increase in speed.

        return a float
        """
        return (299792.458*self.VEL)/self.frequency

    def validate_frequency(self, freq_data):
        """Validate frequency.

        Keyword arguments:
        freq_data -- frequency 73 and 111 GHz

        return a boolean
        """
        if freq_data >= 73 and freq_data <= 111:
            return True
        else:
            return False

    def validate_sensitivity(self, sensitivity_data):
        """Validate sensitivity.

        Keyword arguments:
        sensivity_data -- sensivity > 0

        return a boolean
        """
        if sensitivity_data > 0:
            return True
        else:
            return False
