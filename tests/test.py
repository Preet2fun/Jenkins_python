#!/usr/bin/env python
"""Unit tests for the project1.calculator module."""

from unittest import TestCase
from mock import patch
#import Test_Project.calci

class TestCalculator(TestCase):
	"""abcd... """
    @patch('Test_Project.calci.Calculator.sum', return_value=9)
	""" def... """
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)
