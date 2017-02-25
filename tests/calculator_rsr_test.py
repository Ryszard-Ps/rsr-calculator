# -*- coding: utf-8 -*-
"""Test RSR.

$ python -m unittest discover -v tests -p "*_test.py"
"""
import unittest

from rsr_calculator.rsr import RSR


class TestCalculatorRSR(unittest.TestCase):
    """Test Calculator RSR."""

    VERSION = '1.0.0'
    MODE_DEFAULT = 1
    MODES = [1, 2]

    def setUp(self):
        """Setup."""
        self.calculator = RSR(self.MODE_DEFAULT)

    def test_version(self):
        """Test of the version."""
        self.assertEqual(self.calculator.get_version(), self.VERSION)

    def test_validate_frequency_true(self):
        """Validate frequency True.

        :attention: `subTest` - Not support python < 3.4
        """
        freq_data = [73, 76, 79, 80, 98, 82, 100, 111]
        for i in freq_data:
            # Context accuracy for the error within the subtest i=i or i
            with self.subTest(i=i):
                self.assertTrue(self.calculator.validate_frequency(i))

    def test_validate_frequency_false(self):
        """Validate frequency False.

        :attention: `subTest` - Not support python < 3.4
        """
        freq_data = [1, 0, 15, 23, 72, 112, 113, 150]
        for i in freq_data:
            # Context accuracy for the error within the subtest i=i or i
            with self.subTest(i=i):
                self.assertFalse(self.calculator.validate_frequency(i))

    def test_validate_sensitivity_true(self):
        """Validate sensitivity True.

        :attention: `subTest` - Not support python < 3.4
        """
        sensitivity_data = [1.0, 1, 0.01, 0.2, 0.1, 2.9, 100]
        for i in sensitivity_data:
            # Context accuracy for the error within the subtest i=i or i
            with self.subTest(i=i):
                self.assertTrue(self.calculator.validate_sensitivity(i))

    def test_validate_sensitivity_false(self):
        """Validate sensitivity False.

        :attention: `subTest` - Not support python < 3.4
        """
        sensitivity_data = [-1.0, -1, 0, 0.0, -0.1, -2.9, -100]
        for i in sensitivity_data:
            # Context accuracy for the error within the subtest i=i or i
            with self.subTest(i=i):
                self.assertFalse(self.calculator.validate_sensitivity(i))

    def test_calculator_mk(self):
        """RMS expected in given time, units mK."""
        self.calculator.set_mode(1)
        mk_data = {'mK': '0.63'}
        self.assertDictEqual(self.calculator.calculator(92, 25, 'mK'), mk_data)

    def test_calculator_mjy(self):
        """RMS expected in given time, units mJy."""
        self.calculator.set_mode(1)
        mjy_data = {'mJy': '1.77'}
        self.assertDictEqual(
            self.calculator.calculator(92, 25, 'mJy'), mjy_data
        )

    def test_calculator_temperature(self):
        """Time required for target RMS, units Temperature."""
        self.calculator.set_mode(2)
        temperature_data = {'time': '24.94'}
        self.assertDictEqual(
            self.calculator.calculator(92, 0.63, 'temperature'),
            temperature_data
        )

    def test_calculator_flux(self):
        """Time required for target RMS, units Flux."""
        self.calculator.set_mode(2)
        flux_data = {'time': '24.95'}
        self.assertDictEqual(
            self.calculator.calculator(92, 1.77, 'flux'), flux_data
        )

if __name__ == '__main__':
    unittest.main
