'''
    https://leetcode.com/problems/diameter-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''
            num_e is number of edge
            num_v is number of vertex
        '''
        def dia(_root) -> int:
            if root is None:
                return 0, 0
            num_e_left = 0
            num_e_right = 0
            num_v_left = 0
            num_v_right = 0
            if _root.left:
                num_v_left, num_e_left = dia(_root.left)
            if _root.right:
                num_v_right, num_e_right = dia(_root.right)
            num_v_curr = max(num_v_left, num_v_right) + 1
            num_e_curr = max(num_e_left, num_e_right, num_v_left + num_v_right)
            return num_v_curr, num_e_curr
        return dia(root)[1]
