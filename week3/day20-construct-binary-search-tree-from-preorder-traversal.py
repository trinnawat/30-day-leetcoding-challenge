'''
    https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal
'''


class TreeNode:
    '''
        Definition for a binary tree node.
    '''

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def add_node(root, n):
            if root.val is None:
                root.val = n
            else:
                if n < root.val:
                    if root.left is None:
                        root.left = TreeNode(n)
                    else:
                        add_node(root.left, n)
                elif n > root.val:
                    if root.right is None:
                        root.right = TreeNode(n)
                    else:
                        add_node(root.right, n)
        _root = TreeNode(None)
        for _n in preorder:
            add_node(_root, _n)
        return _root
