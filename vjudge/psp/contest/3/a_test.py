import unittest
import a

class Test(unittest.TestCase):
    def test_limit_low(self):
        self.assertEqual(a.solve())