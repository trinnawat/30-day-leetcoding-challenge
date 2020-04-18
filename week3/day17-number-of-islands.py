'''
    https://leetcode.com/problems/number-of-islands
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        queue = []
        height = len(grid)
        width = len(grid[0])
        count_land = 0

        def find_land(i, j):
            if i < 0 or j < 0 or i == height or j == width or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            find_land(i+1, j)
            find_land(i-1, j)
            find_land(i, j+1)
            find_land(i, j-1)
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    count_land += 1
                    find_land(i, j)
        return count_land
