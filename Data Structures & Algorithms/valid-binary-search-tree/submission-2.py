# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, low, high):
        if low < root.val < high:
            if not root.right and not root.left: return True
            elif not root.right and root.left:
                return self.helper(root.left, low, root.val)
            elif root.right and not root.left:
                return self.helper(root.right, root.val, high)
            return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)
        else: return False
