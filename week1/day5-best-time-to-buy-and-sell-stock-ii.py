'''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        accum_sum = 0
        for i in range(1, len(prices)):
            prev_px = prices[i-1]
            curr_px = prices[i]
            accum_sum += max(curr_px - prev_px, 0)
        return accum_sum
