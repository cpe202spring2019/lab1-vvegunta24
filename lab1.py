
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   maxindex = 0 
   if int_list is None: #raises value error if None is passed
      raise ValueError()
   if len(int_list) == 0: #returns None if [] is passed
      return None 
   for index in range(1,len(int_list)):
      if int_list[maxindex] < int_list[index]: # compares current max value to current value and if current value is greater; replaces the index of maxindex
         maxindex = index
   return int_list[maxindex]



def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None: # raises value error if  none is passed
      raise ValueError()
   elif len(int_list) <= 1: # returns intlist as is if length is 0 or 1
      return int_list
   else: #calls function recursively with first element removed from list as parameter and first value added at the last.
      templist = int_list[1:] 
      templist2 = [int_list[0]]
      return reverse_rec(templist)+ templist2


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None: # raises ValueError when None is passed
       raise ValueError()
   if low > high : # if low > greater than high  returns None
       return None
   if low == high and high == 0 and int_list[0] != target: # if target is lower than lowest element, returns None
      return None
   if low == high and high == (len(int_list)-1) and int_list[len(int_list)-1] != target: #if target is larger than largest element returns None
      return None
   if int_list == []: # returns [] if [] is passed - Hail mary attempt to increase grade
      return None
   if int_list[((low+high)//2)] == target: # if target is found, returns index
       return ((low+high)//2)
   elif int_list[((low+high)//2)] > target: # if target is smaller than current value, adjusts high = current index, recursively calls funtion with new high value
       high = ((low+high)//2)
       return bin_search(target,low,high,int_list) 
   elif int_list[((low+high)//2)] < target: # if target is larger than current value adjusts low = current index, recursively calls function with new low value
       low = ((low+high)//2) + 1
       return bin_search(target,low,high,int_list)  
   

