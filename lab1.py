
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   maxindex = 0
   if int_list is None:
      raise ValueError()
   if len(int_list) == 0:
      return None 
   for index in range(1,len(int_list)):
      if int_list[maxindex] < int_list[index]:
         maxindex = index
   return int_list[maxindex]



def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError()
   elif len(int_list) <= 1:
      return int_list
   else:
      templist = int_list[1:]
      templist2 = [int_list[0]]
      return reverse_rec(templist)+ templist2


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
       raise ValueError()
   if low > high:
       return None
   if int_list[((low+high)//2)] == target:
       return ((low+high)//2)
   elif int_list[((low+high)//2)] >= target:
       high = ((low+high)//2)
       return bin_search(target,low,high,int_list)
   elif int_list[((low+high)//2)] <= target:
       low = ((low+high)//2) + 1
       return bin_search(target,low,high,int_list)
   

