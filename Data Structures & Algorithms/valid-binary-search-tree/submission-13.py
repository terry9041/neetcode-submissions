# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, high):
            # base case: None
            if not root:
                return True

            # reg case: check itself
            if low < root.val < high:
                return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
            else:
                return False
                
        return dfs(root, -1001, 1000)

        # TC: O(n), always the same
        # SC: O(h), worst case is h = n when tree is linear
            