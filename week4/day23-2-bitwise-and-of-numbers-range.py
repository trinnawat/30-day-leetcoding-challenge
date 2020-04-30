'''
    https://leetcode.com/problems/bitwise-and-of-numbers-range
    credit: https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/593298/Python-O(log-n)-Find-Common-Prefix
'''


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count_shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            count_shift += 1
        return m << count_shift
