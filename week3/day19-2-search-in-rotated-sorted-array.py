'''
    https://leetcode.com/problems/search-in-rotated-sorted-array
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_id = 0
        right_id = len(nums) - 1
        while left_id <= right_id:
            mid_id = (right_id + left_id)//2
            if nums[mid_id] == target:
                return mid_id
            if nums[left_id] <= nums[mid_id]:
                if nums[left_id] <= target < nums[mid_id]:
                    right_id = mid_id - 1
                else:
                    left_id = mid_id + 1
            else:
                if nums[mid_id] < target <= nums[right_id]:
                    left_id = mid_id + 1
                else:
                    right_id = mid_id - 1
        return -1
