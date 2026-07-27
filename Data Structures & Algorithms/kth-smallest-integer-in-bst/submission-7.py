# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = self.printNode(root, [])
        return array[k-1]
    
    
    def printNode(self, root, array):
        if root.left:
            self.printNode(root.left, array)
        array.append(root.val)
        if root.right:
            self.printNode(root.right, array)
        return array
        
    