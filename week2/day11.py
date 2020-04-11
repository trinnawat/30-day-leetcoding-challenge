# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def dia(_root) -> int:
            if not _root.left and not _root.right:
                return 0, 0
            dl = 0
            dr = 0
            hl = 0
            hr = 0
            link = 0
            if _root.left:
                hl, dl = dia(_root.left)
                link += 1
            if _root.right:
                hr, dr = dia(_root.right)
                link += 1
            hi = max(hl, hr) + 1
            di = max(dl, dr, hl + hr + link)
            return hi, di
        
        return dia(root)[1]