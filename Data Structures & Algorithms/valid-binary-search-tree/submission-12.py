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

            # 1. check left
            if not inOrder(node.left):
                return False

            # 2. check self, if valid -> update prev max
            if not node.val > self.prev:
                return False
            self.prev = node.val
            
            # 3. check right
            return inOrder(node.right)

        return inOrder(root)

        # TC: O(n), always the same
        # SC: O(h), worst case n = h when linear tree
            