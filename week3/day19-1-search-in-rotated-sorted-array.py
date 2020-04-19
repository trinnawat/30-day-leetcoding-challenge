'''
    https://leetcode.com/problems/search-in-rotated-sorted-array
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        def _search_max_idx(nums, first_id, last_id):
            if first_id == last_id:
                return first_id
            if last_id - first_id == 1:
                if nums[first_id] > nums[last_id]:
                    return first_id
                else:
                    return last_id
            mid_id = ((last_id - first_id)//2) + first_id
            if nums[first_id] < nums[last_id]:
                return last_id
            if nums[first_id] < nums[mid_id]:
                return _search_max_idx(nums, mid_id, last_id)
            else:
                return _search_max_idx(nums, first_id, mid_id)

        def _search(nums, first_id, last_id, target):
            if first_id == last_id:
                if nums[first_id] == target:
                    return first_id
                return -1
            if first_id > last_id:
                return -1

            mid_id = first_id + int((last_id - first_id)/2)
            first = nums[first_id]
            last = nums[last_id]
            mid = nums[mid_id]

            if target == mid:
                return mid_id
            if target == first:
                return first_id
            if target == last:
                return last_id
            if first < target < mid:
                return _search(nums, first_id+1, mid_id-1, target)
            if mid < target < last:
                return _search(nums, mid_id+1, last_id-1, target)
            return -1
        max_id = _search_max_idx(nums, 0, len(nums)-1)
        if max_id == len(nums)-1:
            _mid_id = len(nums)//2
        else:
            _mid_id = max_id + 1
        if nums[0] <= target <= nums[_mid_id-1]:
            return _search(nums, 0, _mid_id-1, target)
        else:
            return _search(nums, _mid_id, len(nums)-1, target)
