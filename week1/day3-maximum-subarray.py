'''
    https://leetcode.com/problems/maximum-subarray
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -2147483647
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum > max_sum:
                max_sum = _sum
            if _sum < 0:
                _sum = 0
        return max_sum
