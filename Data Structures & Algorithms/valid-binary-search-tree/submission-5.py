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
            if not node:
                return True
            
            # 1. Visit Left
            if not inOrder(node.left):
                return False
            
            # 2. Check current node against self.prev
            if self.prev >= node.val:
                return False
            
            # 3. Update self.prev
            self.prev = node.val
            
            # 4. Visit Right
            return inOrder(node.right)

        return inOrder(root)