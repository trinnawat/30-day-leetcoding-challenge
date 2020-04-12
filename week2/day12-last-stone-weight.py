import heapq
'''
    https://leetcode.com/problems/last-stone-weight
'''


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while True:
            if len(stones) < 2:
                break
            first_value = -heapq.heappop(stones)
            next_value = -heapq.heappop(stones)
            diff_value = first_value - next_value
            if diff_value != 0:
                heapq.heappush(stones, -diff_value)

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
