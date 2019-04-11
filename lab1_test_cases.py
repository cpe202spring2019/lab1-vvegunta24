import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertIsNone(max_list_iter([])) #checks for empty list
        self.assertEqual(max_list_iter([1,2,3]),3) #basic tests with highest in different positions
        self.assertEqual(max_list_iter([1,3,2]),3)
        self.assertEqual(max_list_iter([10,6,-3]),10) # basic test for position and chect for negative 
        self.assertEqual(max_list_iter([1,0,0]),1) # checks wether function reacts propperly for duplicate values
        self.assertEqual(max_list_iter([0,1,0]),1) # same as above but with duplicates in different positions
        self.assertEqual(max_list_iter([1,1,0]),1) # checks if duplicates can be max value
        self.assertEqual(max_list_iter([2,2,2,0,1,-1]),2) # multiple duplicates
        self.assertEqual(max_list_iter([0,272,888,888,888,0,0,0]),888) # multiple duplicates with max value in the middle and multiple duplicates of lesser value
        self.assertEqual(max_list_iter([0,0,0,0,0,0,0,0,0,0,]),0) # entire list of same values

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #basic test
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)
        self.assertEqual(reverse_rec([0,0,1,2,3,4]),[4,3,2,1,0,0]) #tests with 2 duplicates
        self.assertEqual(reverse_rec([8,39,-30,5,64]),[64,5,-30,39,8]) #test with randomly ordered numbers
        self.assertEqual(reverse_rec([]),[]) # tests with empty list
        self.assertEqual(reverse_rec([1]),[1]) # tests with sigle number
        self.assertEqual(reverse_rec([0,0,0,0,0,0]),[0,0,0,0,0,0]) # smae values
        self.assertEqual(reverse_rec([1,1,1,0,0,0,3,3,42]),[42,3,3,0,0,0,1,1,1]) #multiple duplicates
        self.assertEqual(reverse_rec([2,3,84,839,20,97294,20,839,84,3,2,1]),[1,2,3,84,839,20,97294,20,839,84,3,2]) #checks for multiple separated repeated values 


    
    
    def test_bin_search(self):
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0,0,10,None)
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        list_val1 = [1,2,3,4,7,8,9,10]
        list_val2 = [0,1,2,3,4,4,4,4,5,6,7]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) # basic test for a middle value
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 ) # basic test for first value
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 ) # basic test for last value
        self.assertEqual(bin_search(9, 0, len(list_val1)-1, list_val1), 6 ) #tests for returning index
        self.assertIsNone(bin_search(11,0,len(list_val)-1,list_val)) # tests with a value that isn't on the list
        self.assertEqual(bin_search(4,0,len(list_val2)-1,list_val2),5) # tests with a list with duplicates
        self.assertEqual(bin_search(1,0,5,[1,1,1,1,1,1]),2) # tests list with same values
        self.assertEqual(bin_search(-1,0,5,[0,1,2,3,4,5]),None)
        self.assertEqual(bin_search(200,0,5,[0,1,2,3,4,5]),None)

if __name__ == "__main__":
        unittest.main()

    
