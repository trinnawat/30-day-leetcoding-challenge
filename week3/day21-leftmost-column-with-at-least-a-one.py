# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()

        # find first row that have 1 in last column
        row_i = 0
        while row_i < n:
            if binaryMatrix.get(row_i, m-1) == 0:
                row_i += 1
            else:
                break
        if row_i == n:
            return -1

        # define binary search for each row

        def binarySearch(l, r, row_num):
            while l < r:
                mid = (l + r) // 2
                if binaryMatrix.get(row_num, mid) == 1:
                    r = mid
                else:
                    l = mid + 1
            return l if binaryMatrix.get(row_num, l) == 1 else -1

        # for each row if the below row is zero then skip that row
        left_most_col = m-1
        while row_i < n:
            if binaryMatrix.get(row_i, left_most_col) == 1:
                col = binarySearch(0, left_most_col, row_i)
                if col < left_most_col:
                    left_most_col = col
            row_i += 1
        return left_most_col
