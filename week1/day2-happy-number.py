'''
    https://leetcode.com/problems/happy-number
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def _is_happy(_n):
            visited.add(_n)
            str_n = str(_n)
            sum_c = 0
            for c in str_n:
                int_c = int(c)
                sum_c += int_c*int_c
            print(sum_c)
            if sum_c == 1:
                return True
            elif sum_c in visited:
                return False
            elif sum_c == 0:
                return False
            else:
                return _is_happy(sum_c)
        return _is_happy(n)
