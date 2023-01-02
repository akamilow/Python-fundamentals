"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""

def first_last6(nums):
  first_num = nums[0]
  last_num = nums[len(nums)-1]
  
  if len(nums) <= 1 and first_num == 6:
    return True
    
  if len(nums) > 1:
    if first_num == 6 or last_num == 6:
      return True

  return False
