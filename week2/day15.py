'''
    https://leetcode.com/problems/product-of-array-except-self
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            output[i] *= left
            output[-i-1] *= right
            left *= nums[i]
            right *= nums[-i-1]
        return output
