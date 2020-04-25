'''
    https://leetcode.com/problems/jump-game
    credit: https://leetcode.com/problems/jump-game/discuss/596454/Python-Simple-solution-with-thinking-process-Runtime-O(n)
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_i = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_i:
                last_i = i
        return last_i == 0
