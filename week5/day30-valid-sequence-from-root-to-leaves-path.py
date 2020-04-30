'''
    Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        def is_valid(node, arr, i):
            if i == len(arr) - 1:
                if node.left is not None or node.right is not None:
                    return False
            if node.val != arr[i]:
                return False
            if node.left is None and node.right is None:
                if i != len(arr) - 1:
                    return False
                return True
            l_valid = r_valid = False
            if node.left is not None:
                l_valid = is_valid(node.left, arr, i+1)
                if l_valid:
                    return l_valid
            if node.right is not None:
                r_valid = is_valid(node.right, arr, i+1)
                if r_valid:
                    return r_valid
            return l_valid or r_valid

        return is_valid(root, arr, 0)
