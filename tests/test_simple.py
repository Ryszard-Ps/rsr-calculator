# -*- coding: utf-8 -*-
"""Test RSR."""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from unittest import TestCase

from should_dsl import should

from rsr_calculator.rsr import RSR


class RSRTest(unittest.TestCase):
    """Test Calculator RSR."""

    def test_version(self):
        """Get version."""
        RSR.get_version() | should | equal_to('0.3.0')

if __name__ == '__main__':
    unittest.main
