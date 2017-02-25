# -*- coding: utf-8 -*-
"""#Calculadora RSR.

**Este modulo nos permite realizar las operaciones para los siguientes modos:**

1. RMS expected in given time.
2. Time required for target RMS.
"""
from math import sqrt

from .version import version


class RSR(object):
    """###Clase de la calculadora `RSR`.

    **Realiza las operaciones para obtener el tiempo
    requerido y el tiempo estimado de una observación.**
    ___
    """

    T_SYS = 100
    VEL = 0.031

    def __init__(self, mode_data=None):
        """###Constructor de la clase `RSR`.

        ** :Parameters: **

        - `mode_data` (int) - Modo de la calculadora (1 y 2)
        ___
        """
        if mode_data is None:
            raise Exception(
                "The input parameters are incorrect {}".format(mode_data)
            )
        else:
            self._mode = mode_data

    def get_version(self):
        """###Retorna la version de la calculadora.

        ** :rtype: str **
        ___
        """
        return version

    def set_mode(self, mode_data):
        """###Actualiza el modo de la calculadora.

        ** :Parameters: **

        - `mode_data` (int) - Modo de la calculadora (1 y 2)
        ___
        """
        self._mode = mode_data

    def calculator(self, freq_data, time_data, unit_data):
        """###Retorna el resultado de un modo y unidad en especifico.

        ** :Parameters: **

        - `freq_data` (int) - Frecuencia entre 73 y 111 (en GHz.).
        - `time_data` (float) - Tiempo de observación (en min.).
        - `unit_data` (str) - Unidades mK, mJy, temperature, flux.

        ** :rtype: ** dict

        **  :note: **Recuerde que `unit_data` es definida de acuerdo al modo.
        ___
        """
        self.frequency = freq_data
        if self._mode == 1:
            if unit_data == 'mK':
                mk = '{0:.2f}'.format(self._calculate_mk(time_data))
                return {'mK': mk}
            elif unit_data == 'mJy':
                mjy = '{0:.2f}'.format(self._calculate_mjy(time_data))
                return {'mJy': mjy}

        elif self._mode == 2:
            if unit_data == 'temperature':
                time = '{0:.2f}'.format(self._calculate_temperature(time_data))
                return {'time': time}
            elif unit_data == 'flux':
                time = '{0:.2f}'.format(self._calculate_flux(time_data))
                return {'time': time}

    def _calculate_mk(self, time_data):
        """###Devuelve el resultado del modo 1 para la unidad mK.

        ** :Parameters: **

        - `time_data` (float) - Tiempo de observación (en min.)

        **:rtype: ** float
        ___
        """
        return (self.T_SYS / 100) * (sqrt(100) / sqrt(self._calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def _calculate_mjy(self, time_data):
        """####Devuelve el resultado del modo 1 para la unidad mJy.

        ** :Parameters: **

        - `time_data` (float) - Tiempo de observación (en min.)

        ** :rtype: ** float
        ___
        """
        return 2.81 * (self.T_SYS / 100) * (sqrt(100) / sqrt(self._calculate_vel())) \
            * sqrt(10) / sqrt(time_data)

    def _calculate_temperature(self, sensitivity_data):
        """###Devuelve el resultado del modo 2 para la unidad temperature.

        ** :Parameters: **

        - `sensitivity_data` (float) - Sensivilidad requerida (en mK.)

        ** :rtype: ** float
        ___
        """
        return (10 * self.T_SYS ** 2) /\
            (100 * self._calculate_vel() * (sensitivity_data ** 2))

    def _calculate_flux(self, sensitivity_data):
        """###Devuelve el resultado del modo 2 para la unidad flux.

        ** :Parameters: **

        - `sensitivity_data` (float) - Sensivilidad requerida (en mJy.)

        ** :rtype: ** float
        ___
        """
        return (78.961 * (self.T_SYS ** 2)) /\
            (100 * self._calculate_vel() * (sensitivity_data ** 2))

    def _calculate_vel(self):
        """###Calcula el aumento en la velocidad.

        ** :rtype: ** float
        ___
        """
        return (299792.458 * self.VEL) / self.frequency

    def validate_frequency(self, freq_data):
        """###Valida la frecuencia.

        ** :Parameters: **

        - `freq_data` (float) - Frecuencia (en GHz.)

        ** :return: ** True si el valor es entre 73 y 111

        ** :rtype: ** bool
        ___
        """
        if freq_data >= 73 and freq_data <= 111:
            return True
        else:
            return False

    def validate_sensitivity(self, sensitivity_data):
        """###Valida la sensivilidad.

        ** :Parameters: **

        - `sensitivity_data` (float) - sensivilidad.

        ** :return: ** True si el valor es mayor que cero.

        ** :rtype: ** bool
        ___
        """
        if sensitivity_data > 0.0:
            return True
        else:
            return False
