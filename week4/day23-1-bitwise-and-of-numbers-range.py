'''
    https://leetcode.com/problems/bitwise-and-of-numbers-range
'''


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        if m == n:
            return m

        def find_factor(num):
            c = 1
            while c <= num:
                c *= 2
            c //= 2
            factor_list = [c]
            rest = num - c
            if rest != 0:
                factor_list += find_factor(rest)
            return factor_list

        factor_list_m = find_factor(m)
        factor_list_n = find_factor(n)
        if factor_list_m[0] == factor_list_n[0]:
            sum_factor = 0
            for i in range(len(factor_list_m)):
                if factor_list_m[i] == factor_list_n[i]:
                    sum_factor += factor_list_m[i]
                else:
                    break
            return sum_factor
        else:
            return 0
