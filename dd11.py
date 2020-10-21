#!usr/bin/python3
#Noel Glamann
#05 November 2019

""" Daily Design #11

Go to CodingBat and do problem sum2 found in the List-1 section
"""

def sum2(nums):
  
  total = 0
  
  if len(nums)>2:
    for i in range(0, 2):
      total += nums[i]
    return total
    
  elif 0 < len(nums) < 3:
    for i in range(0, len(nums)):
      total += nums[i]
    return total
      
  else:
    return 0