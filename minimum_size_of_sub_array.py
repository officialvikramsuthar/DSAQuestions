# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# target = 11
# nums = [1,1,1,1,1,1,1,1]

target = 7
nums = [2,3,1,2,4,3]

import time



def sub_array(target, nums):
    nums.sort()
    start = 0
    end = len(nums) - 1
    index_count = 1
    summ = nums[start]

    while end < len(nums) :
        summ = summ + nums[end]
        index_count += 1

        if nums[start]==target or nums[end] == target:
            return 1

        end += 1

        if summ == target:
            return index_count

        if end == len(nums):
            start += 1
            end = start + 1
            summ = nums[start]
            index_count = 1

        
    return 0

print(sub_array(target= target, nums=nums))

