'''
    https://leetcode.com/problems/maximal-square
'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * (n+1) for _ in range(m+1)]
        max_d = 0
        for i in range(m):
            for j in range(n):
                crr_val = int(matrix[i][j])
                if crr_val == 1:
                    cache[i+1][j+1] = min(cache[i][j],
                                          cache[i][j+1], cache[i+1][j]) + 1
                else:
                    cache[i+1][j+1] = 0
                if cache[i+1][j+1] > max_d:
                    max_d = cache[i+1][j+1]
        return max_d**2
