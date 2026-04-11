# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -1001
        def inOrder(node):
            # base case
            if not node:
                return True

            # check left subtree
            if not inOrder(node.left):
                return False

            # check current node
            # if valid -> update prev
            if node.val <= self.prev:
                return False
            self.prev = node.val

            # check right subtree
            return inOrder(node.right)
    
        return inOrder(root)