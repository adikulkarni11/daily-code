"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 1
        for i in range(len(nums)):
            FinalP = nums[i] -1
            while nums[i] >= 1 and nums[i] <= len(nums) and nums[i] != nums[FinalP]:
                nums[i], nums[FinalP] = nums[FinalP], nums[i]
                FinalP = nums[i] - 1
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return len(nums)+1
    