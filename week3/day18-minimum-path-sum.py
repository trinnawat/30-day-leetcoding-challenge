'''
    https://leetcode.com/problems/minimum-path-sum
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        if len(grid) == 1:
            return sum(grid[0])
        height = len(grid)
        width = len(grid[0])
        L = {}
        for i in range(height):
            for j in range(width):
                key = (i, j)
                if i == 0 and j == 0:
                    L[key] = grid[i][j]
                else:
                    if i == 0 and j != 0:
                        L[key] = grid[i][j] + L[(i, j-1)]
                    elif i != 0 and j == 0:
                        L[key] = grid[i][j] + L[(i-1, j)]
                    else:
                        L[key] = grid[i][j] + min(L[(i, j-1)], L[(i-1, j)])
        return L[key]
