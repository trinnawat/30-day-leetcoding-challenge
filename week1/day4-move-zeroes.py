'''
    https://leetcode.com/problems/move-zeroes/
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        count_zero = 0
        i = 0
        while True:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count_zero += 1
            else:
                i += 1

            if count_zero + i == len_nums:
                break