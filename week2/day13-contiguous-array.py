'''
    https://leetcode.com/problems/contiguous-array
'''


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index_table = {0: -1}
        _sum = 0
        max_01 = 0
        for idx, n in enumerate(nums):
            if n == 0:
                _sum -= 1
            else:
                _sum += 1

            if _sum in index_table:
                max_01 = max(max_01, idx - index_table[_sum])
            else:
                index_table[_sum] = idx
        return max_01
