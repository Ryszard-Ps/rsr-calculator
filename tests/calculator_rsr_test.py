# -*- coding: utf-8 -*-
"""Test RSR.

$ python -m unittest discover -v tests -p "*_test.py" 
"""
import unittest

from rsr_calculator.rsr import RSR
from should_dsl import should


class TestCalculatorRSR(unittest.TestCase):
    """Test Calculator RSR."""

    def test_version(self):
        """Test of the version."""
        calculator0 = RSR(1)
        self.assertEqual(calculator0.get_version(), '0.3.2')

    def test_validate_frequency(self):
        """Validate frequency."""
        calculator0 = RSR(1)
        self.assertFalse(calculator0.validate_frequency(72))
        self.assertTrue(calculator0.validate_frequency(73))
        self.assertTrue(calculator0.validate_frequency(111))
        self.assertFalse(calculator0.validate_frequency(112))

    def test_validate_sensitivity(self):
        """Validate sensitivity."""
        calculator0 = RSR(1)
        self.assertTrue(calculator0.validate_sensitivity(1))
        self.assertFalse(calculator0.validate_sensitivity(0))
        self.assertFalse(calculator0.validate_sensitivity(0.0))

    def test_calculator_mk(self):
        """RMS expected in given time, units mK."""
        calculator1 = RSR(1)
        calculator1.calculator(92,25,'mK') | should | equal_to({'mK': '0.63'})


    def test_calculator_mjy(self):
        """RMS expected in given time, units mJy."""
        calculator1 = RSR(1)
        calculator1.calculator(92,25,'mJy') | should | equal_to({'mJy':'1.77'})

    def test_calculator_temperature(self):
        """Time required for target RMS, units Temperature."""
        calculator2 = RSR(2)
        calculator2.calculator(92,0.63,'temperature') | should | equal_to({'time': '24.94'})

    def test_calculator_flux(self):
        """Time required for target RMS, units Flux."""
        calculator2 = RSR(2)
        calculator2.calculator(92,1.77,'flux') | should | equal_to({'time': '24.95'})


if __name__ == '__main__':
    unittest.main
