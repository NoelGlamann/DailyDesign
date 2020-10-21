#!usr/bin/python3
#Noel Glamann

def max_end3(nums):

  biggest = 0

  if nums[0] > nums[2]:
    biggest += nums[0]
  else:
    biggest += nums[2]

  for i in range(3):
    nums[i] = biggest

  return nums