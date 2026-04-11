# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            # base case
            if not node:
                return True
            
            curr = node.val
            if low < curr < high:
                return dfs(node.left, low, curr) and dfs(node.right, curr, high)
            else:
                return False

        return dfs(root,-1001,1001)

        # TC: O(n), always the same
        # SC: O(n) for call stack, worst case if the tree is linear