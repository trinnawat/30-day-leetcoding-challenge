/*
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
*/

class Solution {
    public int maxProfit(int[] prices) {
        int accum_sum = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                accum_sum += prices[i] - prices[i - 1];
            }
        }
        return accum_sum;
    }
}