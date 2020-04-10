'''
    https://leetcode.com/problems/single-number/
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if i+1 == len(nums):
                return nums[-1]
            if nums[i]-nums[i+1] !=0:
                return nums[i]