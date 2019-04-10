import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([]),None)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)
        self.assertEqual(reverse_rec([0,0,1,2,3,4]),[4,3,2,1,0,0])
        self.assertEqual(reverse_rec([8,39,30,59,64]),[64,59,30,39,8])
    
    
    def test_bin_search(self):
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0,0,10,None)
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        list_val1 = [1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 )
        self.assertEqual(bin_search(9, 0, len(list_val1)-1, list_val1), 6 )

if __name__ == "__main__":
        unittest.main()

    
