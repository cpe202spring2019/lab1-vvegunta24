import unittest
from location import *

loc = Location("SLO", 35.3, -120.7)
loc2 = Location("Paris", 48.9, 2.4)
loc1 = Location("SLO", 35.3, -120.7)
class TestLab1(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2),"Location('Paris', 48.9, 2.4)")
    
    # Add more tests!
    def test_eq(self):
        self.assertEqual(loc,loc1)
        self.assertFalse(loc.__eq__(loc2))
        self.assertNotEqual(loc,loc2)
        self.assertFalse(loc.__eq__("thing"))
        self.assertNotEqual(loc,"thing")

if __name__ == "__main__":
        unittest.main()
