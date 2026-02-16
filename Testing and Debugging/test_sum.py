"""a basic sum function that needs to be tested.
The TestSum class extends the TestCase class and has a test_sum method 
that will verify that the sum function works correctly."""

import unittest

def sum(x, y):
    return x + y

class TestSum(unittest.TestCase):
        def test_sum(self):
            self.assertEqual(sum(2, 3), 5)

unittest.main(exit=False)
