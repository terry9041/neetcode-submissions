# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # TC: O(n), where n is the num of nodes
        # SC: O(n), where n is tree height
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))