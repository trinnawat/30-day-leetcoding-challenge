'''
    https://leetcode.com/problems/binary-tree-maximum-path-sum
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def cal_max_score(_root):
            if not _root.left and not _root.right:
                return _root.val, _root.val
            max_height = max_score = -99999
            l_max_height = l_max_score = -99999
            r_max_height = r_max_score = -99999
            if _root.left is not None:
                l_max_height, l_max_score = cal_max_score(_root.left)
            if _root.right is not None:
                r_max_height, r_max_score = cal_max_score(_root.right)
            max_height = max(l_max_height, r_max_height, 0) + _root.val
            max_score = max(max_height, l_max_score, r_max_score,
                            _root.val + l_max_height + r_max_height)
            return max_height, max_score
        return cal_max_score(root)[1]
