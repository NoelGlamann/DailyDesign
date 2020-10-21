#!/usr/bin/python3
#Noel Glamann
#December 2, 2019

'''daily design 14'''

def make_ends(nums):
    ends = [0, 0]
    if len(nums)>1:
        ends[0] = nums[0]
        ends[1] = nums[-1]
    else:
        ends[0] = nums[0]
        ends[1] = nums[0]
    return ends
