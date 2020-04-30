'''
    https://leetcode.com/problems/subarray-sum-equals-k
    credit: https://leetcode.com/problems/subarray-sum-equals-k/discuss/591831/Python-simple-O(n)-algorithm-explained
'''
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track_sums = defaultdict(int)
        track_sums[0] = 0
        total_sums = 0
        count = 0
        for n in nums:
            total_sums += n
            if total_sums == k:
                count += 1
            if total_sums-k in track_sums:
                count += track_sums[total_sums - k]
            track_sums[total_sums] += 1
        return count
